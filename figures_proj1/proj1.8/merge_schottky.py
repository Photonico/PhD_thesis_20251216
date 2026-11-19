"""Rebuild the vector Schottky figure with Matplotlib and PyMuPDF."""

from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory

import matplotlib
import pymupdf as pdf

matplotlib.use("Agg")
import matplotlib.pyplot as plt

FOLDER = Path(__file__).resolve().parent
OUTPUT = FOLDER / "proj1.8_schottky.pdf"

# Source rectangles use PDF points.
SCHEMATIC = pdf.Rect(34, 26, 408, 261)
CRITERIA = pdf.Rect(428, 85, 765, 225)
BANDS = pdf.Rect(0, 22, 586, 425)
A_SCALE = 0.90


def place(page, source, crop, x, y, scale=1):
    box = pdf.Rect(x, y, x + crop.width * scale, y + crop.height * scale)
    page.show_pdf_page(box, source, 0, clip=crop)


def main():
    source_a = FOLDER / "proj1.8a.pdf"
    if not source_a.is_file():
        source_a = FOLDER / "proj1.8a_backup.pdf"

    left = 10
    right = left + SCHEMATIC.width * A_SCALE + 18
    bands_top, diagram_top = 10, 51
    criteria_top = diagram_top + SCHEMATIC.height * A_SCALE + 2
    width = right + BANDS.width + left
    height = max(bands_top + BANDS.height, criteria_top + CRITERIA.height * A_SCALE) + left

    with (pdf.open(source_a) as diagram, pdf.open(source_a) as criteria,
          pdf.open(FOLDER / "proj1.8b.pdf") as bands, pdf.open() as output):
        diagram[0].clip_to_rect(SCHEMATIC)
        criteria[0].clip_to_rect(CRITERIA)
        bands_page = bands[0]
        bands_page.set_mediabox(pdf.Rect(-12, 0, 576, 432))
        # Clear the old heading above the plot, including its vector subscripts.
        bands_page.add_redact_annot(pdf.Rect(140, 3, 490, 29.5), fill=False)
        bands_page.apply_redactions(images=0, graphics=1)

        page = output.new_page(width=width, height=height)
        place(page, diagram, SCHEMATIC, left, diagram_top, A_SCALE)
        place(page, criteria, CRITERIA, left + 6, criteria_top, A_SCALE)
        place(page, bands, BANDS, right, bands_top)

        with plt.rc_context({"font.family": "serif", "mathtext.fontset": "cm", "pdf.fonttype": 42}):
            figure = plt.figure(figsize=(width / 72, height / 72))
            box = dict(boxstyle="round,pad=0.2", facecolor=(1, 1, 1, .88), edgecolor="#c6c6c6")
            # Place (b) just inside the upper-left corner of the data axes.
            for x, title in ((left + 6, "(a) Schottky barriers"),
                             (right + 63, r"(b) Graphene-B$_4$C$_3$ (HSE06)")):
                figure.text(x / width, 1 - 27 / height, title, fontsize=17,
                            ha="left", va="top", bbox=box)
            headers = BytesIO()
            figure.savefig(headers, format="pdf", transparent=True, metadata={"CreationDate": None})
            plt.close(figure)
        with pdf.open(stream=headers.getvalue(), filetype="pdf") as overlay:
            page.show_pdf_page(page.rect, overlay, 0)

        with TemporaryDirectory(dir=FOLDER) as staging:
            generated = Path(staging) / OUTPUT.name
            output.save(generated, garbage=4, deflate=True, no_new_id=True)
            generated.replace(OUTPUT)
    print(f"{source_a.name} + proj1.8b.pdf -> {OUTPUT.name}")


if __name__ == "__main__":
    main()
