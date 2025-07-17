# Text Extraction Application

A comprehensive Python application that extracts text from various file formats (documents, PDFs, images, and audio) and compiles it into a single text file.

## Features

- **Multi-format Support**: Handles text files, PDFs, images, and audio files
- **OCR Integration**: Uses Tesseract OCR for image-based text extraction
- **Speech-to-Text**: Converts audio files to text using Google Speech Recognition
- **Recursive Processing**: Scans folders recursively for all supported files
- **Error Handling**: Robust error handling with detailed logging
- **Clean Output**: Organized output with file headers and separators

## Supported File Formats

### Text Documents
- `.txt` - Plain text files
- `.md` - Markdown files
- `.rst` - reStructuredText files

### Office Documents
- `.docx` - Microsoft Word documents

### PDFs
- `.pdf` - PDF documents (with OCR fallback for scanned PDFs)

### Images
- `.png` - PNG images
- `.jpg`, `.jpeg` - JPEG images
- `.bmp` - Bitmap images
- `.tiff`, `.tif` - TIFF images
- `.gif` - GIF images

### Audio Files
- `.wav` - WAV audio files
- `.mp3` - MP3 audio files
- `.m4a` - M4A audio files
- `.ogg` - OGG audio files
- `.flac` - FLAC audio files
- `.aac` - AAC audio files

## Installation

### Prerequisites

1. **Python 3.7+** installed on your system
2. **Tesseract OCR** for image and PDF text extraction

### Install Tesseract OCR

#### Windows
1. Download and install Tesseract from [UB-Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
2. Add Tesseract to your PATH environment variable
3. Verify installation: `tesseract --version`

#### macOS
```bash
brew install tesseract
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get install tesseract-ocr
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python extract_folder_text.py <folder_path> <output_file.txt>
```

### Examples

```bash
# Extract text from a documents folder
python extract_folder_text.py ./documents ./output.txt

# Extract text from current directory
python extract_folder_text.py . ./all_text.txt

# Extract text from a specific folder
python extract_folder_text.py /home/user/Documents ./extracted_text.txt
```

### Output Format

The output file will contain:
- A header with extraction details
- Each file's content separated by headers
- File paths for easy reference
- Error messages if any issues occur

Example output:
```
Text Extraction Report
=====================
Source Folder: ./documents
Generated on: output.txt
==================================================

--- ./documents/report.pdf ---
This is the content from the PDF file...
--------------------------------------------------

--- ./documents/image.png ---
[No text detected in image]
--------------------------------------------------
```

## Configuration

### Custom Tesseract Path

If Tesseract is not in your PATH, you can specify its location:

```python
# Add this line before using pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### Logging

The application uses Python's logging module. To change log level:

```python
import logging
logging.getLogger().setLevel(logging.DEBUG)  # or logging.WARNING
```

## Troubleshooting

### Common Issues

1. **Tesseract not found**
   - Ensure Tesseract is installed and in PATH
   - Check installation with `tesseract --version`

2. **Audio files not processing**
   - Ensure audio files are not corrupted
   - Check internet connection for Google Speech API

3. **PDF processing errors**
   - Some PDFs may be password-protected
   - Try converting to images first if issues persist

4. **Memory issues with large files**
   - Process files in smaller batches
   - Consider splitting large PDFs

### Performance Tips

- Process smaller folders first to test functionality
- Use SSD storage for better I/O performance
- Close other applications to free up memory
- Consider using multiprocessing for large datasets

## Development

### Project Structure
```
text-extraction-app/
├── extract_folder_text.py    # Main application
├── requirements.txt          # Python dependencies
├── README.md                # This file
└── examples/                # Example files (optional)
```

### Adding New File Types

To add support for new file types:

1. Create a new extraction function
2. Add the file extension to `FILE_TYPES` dictionary
3. Test with sample files

Example:
```python
def extract_text_from_csv(file_path: str) -> str:
    # Your implementation here
    pass

FILE_TYPES['.csv'] = extract_text_from_csv
```

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.
