"""Execute and verify the Chapter 4 schematics from both supported folders."""

import hashlib
import json
from pathlib import Path

import nbformat
from nbclient import NotebookClient


ROOT = Path(__file__).resolve().parents[2]
NOTEBOOK = ROOT / "figures_ch4/figures_ch4.ipynb"
AUDIT = Path(__file__).resolve().parent

CHECKS = r'''
import json

gaps = []
for lower, upper in models:
    direct_min = float(np.min(upper - lower))
    indirect = float(np.min(upper) - np.max(lower))
    assert np.all(upper >= lower)
    assert np.allclose([lower[0], upper[0]], [lower[-1], upper[-1]])
    gaps.append((direct_min, indirect))
assert np.allclose(gaps, [(1.20, .76), (.70, -.90), (0., 0.), (.85, .85)], atol=1e-12)
internal_pair = -.65 - .35 * np.abs(np.cos(k))
assert np.all(internal_pair <= models[3][0])
contacts = np.flatnonzero(np.isclose(internal_pair, models[3][0], atol=1e-12))
assert np.allclose(k[contacts], [-np.pi / 2, np.pi / 2])
assert np.allclose(internal_pair[contacts], -.65)
assert np.min(models[3][1] - models[3][0]) > 0

def trim_class(basis, point):
    fractional = np.linalg.solve(basis, point)
    twice = 2 * fractional
    assert np.allclose(twice, np.rint(twice), atol=1e-12)
    return tuple((np.rint(twice).astype(int) % 2).tolist())

trim_results = {}
for name, basis, points, copies in [
        ("triangular", triangular_basis, triangular_points, triangular_copies),
        ("square", square_basis, square_points, square_copies)]:
    classes = [trim_class(basis, point) for point in points]
    assert len(set(classes)) == 4
    assert set(classes) == {(0, 0), (1, 0), (0, 1), (1, 1)}
    for original, point in copies:
        assert trim_class(basis, point) == classes[original]
        difference = np.linalg.solve(basis, point - points[original])
        assert np.allclose(difference, np.rint(difference), atol=1e-12)
    trim_results[name] = {"classes": classes, "periodic_copies": len(copies)}

triangular_normals = np.array([[1., 0.], [.5, np.sqrt(3) / 2],
                               [-.5, np.sqrt(3) / 2]])
assert np.all(np.abs(triangular_points @ triangular_normals.T) <= .5 + 1e-12)
assert np.all(np.abs(square_points) <= .5 + 1e-12)
assert np.allclose(np.max(np.abs(hexagon @ triangular_normals.T), axis=1), .5)
print("SCHEMATIC_AUDIT=" + json.dumps({
    "gaps": gaps, "internal_contacts": k[contacts].tolist(),
    "trim": trim_results, "palette": colors,
    "canvas_inches": {"band": band_size, "trim": trim_size},
    "canvas_dpi": {"band": dpi, "trim": dpi},
    "style_source": "figures_ch4/figures_ch4.ipynb",
    "font_settings": params, "subtitle_fontsize": subtitle,
    "line_width": line_width
}))
'''


def hashes():
    return {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted((ROOT / "figures_ch4").glob("*.pdf"))}


def main():
    source = nbformat.read(NOTEBOOK, as_version=4)
    original_cell_count = len(source.cells)
    assert [cell.source for cell in source.cells if cell.cell_type == "markdown"] == [
        "# Figures of chapter 4", "## 4.1 Band subspace",
        "## 4.2 Time-reversal invariant momenta"]
    assert all("assert " not in cell.source for cell in source.cells)
    reports = {}
    final_notebook = None
    for name, directory in [("repository_root", ROOT),
                            ("figures_folder", NOTEBOOK.parent)]:
        notebook = nbformat.reads(nbformat.writes(source), as_version=4)
        notebook.cells.append(nbformat.v4.new_code_cell(CHECKS))
        NotebookClient(notebook, timeout=120, kernel_name="python3",
                       resources={"metadata": {"path": str(directory)}}).execute()
        stream = "".join(output.get("text", "")
                         for output in notebook.cells[-1].outputs)
        line = next(line for line in stream.splitlines()
                    if line.startswith("SCHEMATIC_AUDIT="))
        reports[name] = json.loads(line.split("=", 1)[1])
        reports[name]["pdf_sha256"] = hashes()
        notebook.cells = notebook.cells[:original_cell_count]
        for cell in notebook.cells:
            if cell.cell_type == "code":
                assert cell.execution_count is not None
                assert not any(output.output_type == "error" for output in cell.outputs)
        final_notebook = notebook
        print(f"{name}: fresh-kernel execution and all assertions passed")

    assert reports["repository_root"]["pdf_sha256"] == reports["figures_folder"]["pdf_sha256"]
    reports["pdfs_identical_between_working_directories"] = True
    nbformat.validate(final_notebook)
    nbformat.write(final_notebook, NOTEBOOK)
    (AUDIT / "schematic_verification.json").write_text(json.dumps(reports, indent=2) + "\n")
    for panel, gap in zip("abcd", reports["repository_root"]["gaps"]):
        print(f"({panel}) minimum direct gap = {gap[0]:.6f}; global gap = {gap[1]:.6f}")
    print("Both PDF files are byte-identical between the two fresh executions.")


if __name__ == "__main__":
    main()
