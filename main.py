import io
from PIL import Image
from pdf2image import convert_from_path
import img2pdf

def convert_slides(input_pdf, output_pdf, dpi=300):
    # Convert PDF to images
    images = convert_from_path(input_pdf, dpi=dpi)
    
    # A4 portrait dimensions at 300 DPI
    a4_width = 2480    # 8.27" * 300
    a4_height = 3508   # 11.69" * 300
    
    output_pages = []
    
    for i in range(0, len(images), 3):
        group = images[i:i+3]
        composite = Image.new('RGB', (a4_width, a4_height), 'white')
        y_position = 0
        
        # Calculate target height per slide (exactly 1/3 of A4 height)
        slide_height = a4_height // 3
        
        for img in group:
            # Convert to RGB if needed
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            
            # Calculate scaling to get exact slide height
            original_width, original_height = img.size
            scale_factor = slide_height / original_height
            new_width = int(original_width * scale_factor)
            new_height = slide_height  # Enforce exact height
            
            # Resize image
            img = img.resize((new_width, new_height), Image.LANCZOS)
            
            # Calculate horizontal positioning
            if new_width > a4_width:
                # Scale down to fit width (maintains aspect ratio)
                scale_factor = a4_width / original_width
                new_width = a4_width
                new_height = int(original_height * scale_factor)
                img = img.resize((new_width, new_height), Image.LANCZOS)
                
            x_position = (a4_width - new_width) // 2  # Center horizontally
            
            # Paste image
            composite.paste(img, (x_position, y_position))
            y_position += new_height  # Stack vertically without spacing
        
        output_pages.append(composite)
    
    # Convert images to PDF
    with open(output_pdf, "wb") as f:
        images_bytes = []
        for page in output_pages:
            img_byte_arr = io.BytesIO()
            page.save(img_byte_arr, format='JPEG', dpi=(dpi, dpi), quality=100)
            images_bytes.append(img_byte_arr.getvalue())
        f.write(img2pdf.convert(images_bytes))

if __name__ == "__main__":
    input_pdf = "input_slides.pdf"
    output_pdf = "output_3up_exact.pdf"
    convert_slides(input_pdf, output_pdf)
    print(f"Created {output_pdf} with exact height matching A4")