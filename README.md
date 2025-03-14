# PDF Slide Merger

## Description
This program processes PDF slides and combines three slides per A4-sized page in portrait orientation. It is useful for saving paper and organizing slides efficiently. The output is a single PDF file with multiple slides per page.

---

## Features
- Converts PDF slides into images.
- Arranges 3 slides per A4-sized page.
- Automatically resizes and centers slides for a professional look.
- Works with both single and multiple PDF files.
- User-friendly input prompts to guide you through the process.

---

## Prerequisites
Before running the program, ensure you have the following installed:
- **Python 3.6 or later**
- Required Python libraries:
  - `Pillow` (for image processing)
  - `pdf2image` (for converting PDFs to images)
  - `img2pdf` (for creating the final PDF)
  
To install them, run the following command in your terminal or command prompt:
```sh
pip install pillow pdf2image img2pdf
```

Additionally, **Poppler** is required for `pdf2image`. Install it using:
- **Windows:** [Download Poppler](https://blog.alivate.com.au/poppler-windows/)
- **Mac (via Homebrew):** `brew install poppler`
- **Linux:** `sudo apt install poppler-utils`

---

## How to Use
1. **Run the script**
   - Open a terminal or command prompt and navigate to the script’s location.
   - Run the script using:
     ```sh
     python script.py
     ```

2. **Follow the prompts**
   - The program will ask if you're ready to proceed. Type `y` to continue.
   - Enter the path to a **single PDF file** or a **folder containing multiple PDFs**.
   - Enter the desired output folder where the final PDF will be saved.
   - Enter a name for the output file (without the `.pdf` extension).

3. **Processing**
   - The program will extract slides from the PDFs and merge them.
   - The progress will be displayed on the screen.

4. **Completion**
   - The merged PDF will be saved in the specified output folder.
   - A success message will confirm the process is complete.

---

## Example
**Input:**
- A folder with 6 slide PDFs.

**Output:**
- A single PDF with 2 pages, each containing 3 slides in portrait layout.

---

## Troubleshooting
### Error: `The specified path does not exist`
- Ensure the file or folder path is correct.
- Use absolute paths (e.g., `C:\Users\YourName\Documents\slides.pdf`).

### Error: `No PDF files found`
- If you entered a folder, check that it contains PDFs.

### Output PDF does not look right
- Ensure the input slides are in a compatible format.
- Try using a higher DPI setting in the script.

---

## Additional Notes
- The script processes slides at **300 DPI** for good quality.
- Adjust the `dpi` parameter in the script for better quality or faster performance.
- The script handles **RGB and RGBA** images automatically.
- Make sure Poppler is installed and correctly configured.

---

## License
This project is open-source. Feel free to modify and use it as needed.

