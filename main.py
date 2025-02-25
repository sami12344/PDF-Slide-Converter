import os
import io
from PIL import Image
from pdf2image import convert_from_path
import img2pdf

def process_slides_to_pdf(slides, output_path, dpi=300):
    """Process a list of slides into a PDF with 3 slides per A4 page"""
    A4_WIDTH, A4_HEIGHT = 2480, 3508  # 8.27" x 11.69" @300DPI
    SLIDES_PER_PAGE = 3
    output_pages = []

    for i in range(0, len(slides), SLIDES_PER_PAGE):
        page = Image.new('RGB', (A4_WIDTH, A4_HEIGHT), (255, 255, 255))
        y_cursor = 0
        
        for slide in slides[i:i+SLIDES_PER_PAGE]:
            if slide.mode == 'RGBA':
                slide = slide.convert('RGB')
            
            orig_width, orig_height = slide.size
            target_height = A4_HEIGHT // SLIDES_PER_PAGE
            
            # Calculate scaling
            scale_factor = target_height / orig_height
            scaled_width = int(orig_width * scale_factor)
            
            if scaled_width > A4_WIDTH:
                scale_factor = A4_WIDTH / orig_width
                scaled_width = A4_WIDTH
                target_height = int(orig_height * scale_factor)
            
            resized = slide.resize((scaled_width, target_height), Image.LANCZOS)
            x_pos = (A4_WIDTH - scaled_width) // 2
            page.paste(resized, (x_pos, y_cursor))
            y_cursor += target_height
        
        output_pages.append(page)

    # Save final PDF
    with open(output_path, "wb") as f:
        images_bytes = []
        for img in output_pages:
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='JPEG', quality=95, dpi=(dpi, dpi))
            images_bytes.append(img_byte_arr.getvalue())
        
        pdf_bytes = img2pdf.convert(images_bytes, layout_fun=img2pdf.get_layout_fun(
            (img2pdf.in_to_pt(8.27), img2pdf.in_to_pt(11.69))
        ))
        f.write(pdf_bytes)

def main():
    print("=== PDF Slide Merger ===")
    print("This program will merge 3 slides per A4 page in portrait orientation")
    
    # Confirmation
    if input("Are you ready to proceed? (y/n): ").lower() != 'y':
        print("Operation cancelled.")
        return

    # Input handling
    input_path = input("Enter path to PDF file or directory containing PDFs: ").strip()
    if not os.path.exists(input_path):
        print("Error: The specified path does not exist")
        return

    # Output handling
    output_dir = input("Enter output directory path: ").strip()
    os.makedirs(output_dir, exist_ok=True)
    
    output_name = input("Enter output filename (without extension): ").strip()
    if not output_name.endswith('.pdf'):
        output_name += '.pdf'
    output_path = os.path.join(output_dir, output_name)

    # Collect PDF files
    pdf_files = []
    if os.path.isfile(input_path):
        pdf_files = [input_path]
    else:
        pdf_files = [os.path.join(input_path, f) 
                    for f in os.listdir(input_path) 
                    if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print("Error: No PDF files found in the specified location")
        return

    # Process all slides
    all_slides = []
    for pdf_file in pdf_files:
        print(f"Processing {os.path.basename(pdf_file)}...")
        all_slides.extend(convert_from_path(pdf_file, dpi=300, fmt='jpeg'))

    # Create output PDF
    print(f"\nMerging {len(all_slides)} slides into {output_path}...")
    process_slides_to_pdf(all_slides, output_path)
    
    print(f"Successfully created merged PDF with {len(all_slides)//3 + (1 if len(all_slides)%3 else 0)} pages")

if __name__ == "__main__":
    main()