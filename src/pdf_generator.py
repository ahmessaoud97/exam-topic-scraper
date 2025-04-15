import os
from fpdf import FPDF
from typing import List, Tuple


def generate_pdf(pages: List[Tuple[str, str]], output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    for title, content in pages:
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)
        pdf.multi_cell(0, 10, title)

        pdf.ln(5)
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 10, content)

    pdf.output(output_path)
    print(f"✅ PDF generated at: {output_path}")
