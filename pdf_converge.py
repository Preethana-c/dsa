import fitz  # PyMuPDF
import os

output_pdf = "consolidated_certificates.pdf"

# Create merged PDF
final_doc = fitz.open()

# Get all PDFs in current folder
pdf_files = [
    f for f in os.listdir(".")
    if f.lower().endswith(".pdf") and f != output_pdf
]

pdf_files.sort()

print("PDFs found:")
for pdf in pdf_files:
    print("-", pdf)

# Reference size from first certificate
first_pdf = fitz.open(pdf_files[0])
reference_rect = first_pdf[0].rect
ref_width = reference_rect.width
ref_height = reference_rect.height
first_pdf.close()

print(f"\nUsing standard size: {ref_width} x {ref_height}")

for pdf_path in pdf_files:
    src = fitz.open(pdf_path)

    for page in src:
        # Create page with standard certificate size
        new_page = final_doc.new_page(
            width=ref_width,
            height=ref_height
        )

        orig_rect = page.rect

        # Scale page to fit while keeping aspect ratio
        scale = min(
            ref_width / orig_rect.width,
            ref_height / orig_rect.height
        )

        new_width = orig_rect.width * scale
        new_height = orig_rect.height * scale

        # Center content
        x0 = (ref_width - new_width) / 2
        y0 = (ref_height - new_height) / 2

        target_rect = fitz.Rect(
            x0,
            y0,
            x0 + new_width,
            y0 + new_height
        )

        # Insert scaled page
        new_page.show_pdf_page(target_rect, src, page.number)

    src.close()

# Save merged PDF
final_doc.save(output_pdf)
final_doc.close()

print(f"\nDone! Created '{output_pdf}'")