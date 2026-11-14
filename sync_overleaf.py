#!/usr/bin/env python
"""One-time reset: make the Overleaf files equal to the commit Overleaf's
GitHub Sync last synchronized with (9b0baa0). Overleaf then has no changes of
its own, so "Pull GitHub changes into Overleaf" brings in the latest GitHub
main without asking to push anything back. Local files, refs, and the index
are not changed; the token is read hidden and passed only on curl's stdin."""
import base64
import getpass
import hashlib
import json
import os
from pathlib import Path
import re
import struct
import subprocess
import sys
import tempfile

REPO = Path(__file__).resolve().parent
ENDPOINT = 'https://git.overleaf.com/670cb15e059a397a1f6cfad1'
SYNC_POINT = '9b0baa0fc02580834874b0ffc676ff5438c0a7ef'      # GitHub Sync base on Overleaf
SYNC_TREE = '2ade16595caf23e541c63f9666c138ef17a05a10'
KNOWN_TREES = ['39ee8bc9ad23b4a9d61e6d9d97dd8ec81cf8a7cd',     # Overleaf content verified 14 Nov 08:36
               '583cf5c598a3746d1e2a1ab71e42bd4e4dfeacef']     # older Overleaf snapshot
LAST_TIP = '8d35fb4a280d4c89830496ea72f44cf6c78a8896'          # Overleaf tip after that sync
SHA = re.compile(r'^[0-9a-f]{40}$')
env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
env.update(GIT_OPTIONAL_LOCKS='0', GIT_TERMINAL_PROMPT='0')


class Stop(Exception):
    pass


def git(args, data=None, git_dir=None):
    cmd = ['git', '--no-optional-locks'] + (['--git-dir=' + str(git_dir)] if git_dir else ['-C', str(REPO)])
    p = subprocess.run(cmd + args, input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, timeout=120)
    if p.returncode:
        raise Stop('git ' + args[0] + ' failed: ' + p.stderr.decode(errors='replace').strip()[-300:])
    return p.stdout


def tree_objects(tree):
    objects = {tree}
    for entry in git(['ls-tree', '-r', '-t', '-z', tree]).split(b'\0'):
        if entry:
            meta = entry.split(b'\t', 1)[0].split()
            if meta[1] not in (b'tree', b'blob'):
                raise Stop('Unsupported object type (for example a submodule).')
            objects.add(meta[2].decode())
    return objects


def request(authorization, suffix, data=None, probe=False):
    headers = {'Cache-Control': 'no-cache', 'User-Agent': 'git/2.53.0'}
    if authorization:
        headers['Authorization'] = authorization
    if data is None:
        headers['Accept'] = 'application/x-git-receive-pack-advertisement'
    else:
        headers['Content-Type'] = 'application/x-git-receive-pack-request'
        headers['Accept'] = 'application/x-git-receive-pack-result'
    config = ''.join('header = ' + json.dumps(k + ': ' + v) + '\n' for k, v in headers.items()).encode()
    cmd = ['/usr/bin/curl', '--disable', '--config', '-', '--silent', '--show-error', '--http1.1',
           '--connect-timeout', '20', '--max-time', '300', '--write-out', '\n%{http_code}',
           '--url', ENDPOINT + suffix]
    payload = None
    try:
        if data is not None:
            fd, payload = tempfile.mkstemp(prefix='overleaf-reset-')
            with os.fdopen(fd, 'wb') as f:
                f.write(data)
            cmd += ['--request', 'POST', '--data-binary', '@' + payload]
        r = subprocess.run(cmd, input=config, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=330)
    except subprocess.TimeoutExpired:
        raise Stop('Overleaf connection timed out.') from None
    finally:
        if payload and os.path.exists(payload):
            os.unlink(payload)
    if r.returncode:
        detail = r.stderr.decode(errors='replace')
        raise Stop('Overleaf connection failed (curl exit {}): {}'.format(
            r.returncode, detail.replace(authorization or '\0', '[redacted]')[:300]))
    body, _, status = r.stdout.rpartition(b'\n')
    code = int(status) if status.isdigit() else 0
    if probe and code in (200, 401, 403):
        return body
    if code in (401, 403):
        raise Stop('Overleaf rejected the token (HTTP {}).'.format(code))
    if code != 200:
        raise Stop('Overleaf request failed (HTTP {}).'.format(code))
    return body


def packets(data):
    out, pos = [], 0
    while pos < len(data):
        size = int(data[pos:pos + 4], 16)
        pos += 4
        if size == 0:
            out.append(None)
            continue
        out.append(data[pos:pos + size - 4])
        pos += size - 4
    return out


def advertise(authorization):
    pkts = packets(request(authorization, '/info/refs?service=git-receive-pack'))
    if len(pkts) < 3 or pkts[0] != b'# service=git-receive-pack\n':
        raise Stop('Unexpected Overleaf advertisement.')
    refs, caps = {}, set()
    for p in pkts[2:]:
        if p is None:
            continue
        line = p.rstrip(b'\n')
        if b'\0' in line:
            line, c = line.split(b'\0', 1)
            caps.update(c.decode().split())
        sha, ref = line.decode().split(' ', 1)
        refs[ref] = sha
    if 'report-status' not in caps:
        raise Stop('Overleaf does not report push status; stopped before upload.')
    branches = [r for r in ('refs/heads/main', 'refs/heads/master') if r in refs]
    if len(branches) != 1:
        raise Stop('Overleaf branch is missing or ambiguous: {}'.format(sorted(refs)))
    return branches[0], refs[branches[0]]


def pkt(payload):
    return '{:04x}'.format(len(payload) + 4).encode() + payload


def main():
    dry = '--dry-run' in sys.argv
    if git(['rev-parse', SYNC_POINT + '^{tree}']).decode().strip() != SYNC_TREE:
        raise Stop('Sync point tree mismatch.')
    github = [l.split()[0] for l in git(['ls-remote', 'origin', 'refs/heads/main']).decode().splitlines()]
    if len(github) != 1 or subprocess.run(['git', '-C', str(REPO), 'merge-base', '--is-ancestor', SYNC_POINT, github[0]],
                                          env=env).returncode:
        raise Stop('GitHub main does not contain the sync point; the web Pull would not apply cleanly.')
    print('GitHub main: {} (contains sync point {})'.format(github[0][:7], SYNC_POINT[:7]))
    known = set()
    for tree in KNOWN_TREES:
        if git(['cat-file', '-t', tree]).decode().strip() == 'tree':
            known |= tree_objects(tree)
    wanted = tree_objects(SYNC_TREE)
    request(None, '/info/refs?service=git-receive-pack', probe=True)
    print('Connection to Overleaf OK.')
    if dry:
        authorization, branch, old = None, 'refs/heads/main', LAST_TIP
    else:
        if not sys.stdin.isatty():
            raise Stop('Run this in a terminal so the token can be typed hidden.')
        token = getpass.getpass('Overleaf Git token (hidden): ').strip()
        if not token:
            raise Stop('No token entered.')
        authorization = 'Basic ' + base64.b64encode(('git:' + token).encode()).decode()
        del token
        branch, old = advertise(authorization)
        print('Overleaf {} is at {}{}'.format(branch, old[:7], '' if old == LAST_TIP else
                                              ' (changed since 14 Nov 08:36; it will be overwritten)'))
    ident = git(['var', 'GIT_COMMITTER_IDENT']).decode().strip()
    with tempfile.TemporaryDirectory(prefix='overleaf-reset-git-') as d:
        bare = Path(d) / 'objects.git'
        subprocess.run(['git', 'init', '--bare', '--quiet', str(bare)], check=True, env=env)
        objects_dir = git(['rev-parse', '--path-format=absolute', '--git-path', 'objects']).decode().strip()
        (bare / 'objects' / 'info' / 'alternates').write_text(objects_dir + '\n')
        raw = ('tree {}\nparent {}\nauthor {}\ncommitter {}\n\nReset to GitHub sync point {}\n'
               .format(SYNC_TREE, old, ident, ident, SYNC_POINT[:7])).encode()
        new = git(['hash-object', '-t', 'commit', '-w', '--stdin'], raw, git_dir=bare).decode().strip()
        ids = [new] + sorted(wanted - known)
        pack = git(['pack-objects', '--stdout', '--window=0'], ('\n'.join(ids) + '\n').encode(), git_dir=bare)
        if pack[:4] != b'PACK' or struct.unpack('>II', pack[4:12]) != (2, len(ids)) \
                or hashlib.sha1(pack[:-20]).digest() != pack[-20:]:
            raise Stop('Pack verification failed.')
        print('Prepared {} objects, {:,} bytes.'.format(len(ids), len(pack)))
        if dry:
            print('Dry run: nothing uploaded.')
            return
        body = pkt('{} {} {}\0report-status\n'.format(old, new, branch).encode()) + b'0000' + pack
        reports = [p.rstrip(b'\n') for p in packets(request(authorization, '/git-receive-pack', body)) if p]
        if b'unpack ok' not in reports or ('ok ' + branch).encode() not in reports:
            raise Stop('Overleaf rejected the update: {}'.format(reports))
        if advertise(authorization) != (branch, new):
            raise Stop('Upload accepted but the Overleaf tip differs; check before retrying.')
    print('Success: Overleaf files now equal sync point {}.'.format(SYNC_POINT[:7]))
    print('Next: in Overleaf open Sync with GitHub and click "Pull GitHub changes into Overleaf".')


if __name__ == '__main__':
    try:
        main()
    except Stop as e:
        print('Stopped:', e)
        sys.exit(1)
    except KeyboardInterrupt:
        print('\nInterrupted.')
        sys.exit(130)
