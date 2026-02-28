import fitz  # PyMuPDF

output_pdf_final = "output_marks.pdf"
final_doc = fitz.open()

# Standard A4 size
a4_rect = fitz.paper_rect("a4")

def add_pdf_standardized(pdf_path):
    src = fitz.open(pdf_path)
    
    for page in src:
        new_page = final_doc.new_page(width=a4_rect.width, height=a4_rect.height)
        
        # Get original page size
        orig_rect = page.rect
        
        # Calculate scaling factor (keep aspect ratio)
        scale = min(
            a4_rect.width / orig_rect.width,
            a4_rect.height / orig_rect.height
        )
        
        # Calculate new dimensions
        new_width = orig_rect.width * scale
        new_height = orig_rect.height * scale
        
        # Center on A4 page
        x0 = (a4_rect.width - new_width) / 2
        y0 = (a4_rect.height - new_height) / 2
        target_rect = fitz.Rect(x0, y0, x0 + new_width, y0 + new_height)
        
        new_page.show_pdf_page(target_rect, src, page.number)

# Add your PDFs (in order)
add_pdf_standardized("Preethana_10th_marksheet.pdf")
add_pdf_standardized("Preethana_12th_marksheet.pdf")
add_pdf_standardized("college_trans.pdf")

final_doc.save(output_pdf_final)
print("Done! All pages standardized to A4.")