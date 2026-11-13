"""Compile Chapter 4 with the current thesis preamble and external references."""

from pathlib import Path
import subprocess


root = Path(__file__).resolve().parents[2]
output = root / ".output" / "ch4-draft"
output.mkdir(parents=True, exist_ok=True)
auxiliary = root / ".output" / "thesis.aux"
if not auxiliary.exists():
    raise SystemExit("Compile thesis.tex first to resolve references to existing chapters.")

preamble = (root / "thesis.tex").read_text().split(r"\begin{document}", 1)[0]
hyperref = r"\usepackage[pdftex,bookmarks=true]{hyperref}"
if hyperref not in preamble:
    raise SystemExit("The thesis hyperref setup changed; update the draft wrapper.")
preamble = preamble.replace(hyperref, r"\usepackage{xr-hyper}" + "\n" + hyperref)

# The class's tocindent labels are layout dimensions, not cross-references.
labels = [
    line for line in auxiliary.read_text().splitlines()
    if line.startswith(r"\newlabel{")
    and not line.startswith(r"\newlabel{tocindent")
]
(output / "reference_labels.aux").write_text("\n".join(labels) + "\n")

body = r"""
\externaldocument{.output/ch4-draft/reference_labels}[../thesis.pdf]
\hypersetup{pdftitle={Fundamentals III: Band Topology - Chapter 4 draft}}
\begin{document}
\linespread{1.25}\selectfont
\setupParagraphs
\pagestyle{headings}
\setcounter{chapter}{3}
\setcounter{page}{1}
\input{src/fundamentals_c.tex}
\clearpage
\printbibliography[title={References}]
\end{document}
"""
(output / "fundamentals_c_draft.tex").write_text(preamble + body)
with (output / "build.log").open("w") as log:
    subprocess.run(
        [
            "latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error",
            "-file-line-error", "-outdir=.output/ch4-draft",
            ".output/ch4-draft/fundamentals_c_draft.tex",
        ],
        cwd=root, stdout=log, stderr=subprocess.STDOUT, check=True,
    )
print(output / "fundamentals_c_draft.pdf")
