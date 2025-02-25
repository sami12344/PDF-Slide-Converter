# PDF Slide Converter

## Overview

This script converts a PDF containing slides into a new PDF where each page consists of three slides arranged vertically. The output pages are formatted to fit exactly within A4-sized pages (8.27" x 11.69" at 300 DPI), ensuring a professional layout with consistent sizing.

## Features

- Converts slides from a PDF into images
- Arranges three slides per A4 page in portrait orientation
- Ensures slides are evenly distributed across the page
- Maintains high image quality using 300 DPI resolution
- Outputs a new PDF with properly formatted slides

## Prerequisites

Ensure you have the following dependencies installed:

```sh
pip install pillow pdf2image img2pdf
```

You also need `poppler` installed to convert PDF pages into images. Install it using:

- **Windows:** Download from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases) and add it to your system `PATH`.
- **macOS (Homebrew):**
  ```sh
  brew install poppler
  ```
- **Linux (Debian/Ubuntu):**
  ```sh
  sudo apt install poppler-utils
  ```

## Usage

1. Place the input PDF file in the same directory as the script.
2. Run the script using:

   ```sh
   python script.py
   ```

3. The output PDF will be generated as `output_3up_exact.pdf`.

## Code Explanation

- **`convert_from_path(input_pdf, dpi=300)`**: Converts each page of the input PDF into an image at 300 DPI.
- **Resizing & Scaling**: Ensures each slide is exactly one-third the height of an A4 page while maintaining aspect ratio.
- **`Image.new('RGB', (a4_width, a4_height), 'white')`**: Creates a blank white A4-sized canvas to arrange slides.
- **`img.resize((new_width, new_height), Image.LANCZOS)`**: Resizes images smoothly while maintaining quality.
- **`img2pdf.convert(images_bytes)`**: Combines processed images into a new PDF file.

## Customization

- Adjust `dpi` in `convert_slides()` to change the resolution.
- Modify `a4_width` and `a4_height` to change the output page size.
- Change `output_pdf` filename in the script to customize the output file name.

## Notes

- Ensure your input PDF contains slides in landscape mode for optimal formatting.
- The script automatically centers each slide and ensures an equal vertical distribution.
- If the slide aspect ratio does not fit perfectly, the script will resize while maintaining as much of the original proportion as possible.

## License

This script is provided under the MIT License. Feel free to modify and use it as needed.
