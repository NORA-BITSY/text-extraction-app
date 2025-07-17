#!/usr/bin/env python3
"""
Text Extraction Tool
Extracts text from various file formats (documents, PDFs, images, audio) 
and compiles it into a single text file.

Usage:
    python extract_folder_text.py <folder_path> <output_file.txt>
"""

import os
import sys
import logging
from pathlib import Path
import pytesseract
from PIL import Image
import pdfplumber
import docx
import speech_recognition as sr
from pydub import AudioSegment
import tempfile

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Supported file extensions and their handlers
FILE_HANDLERS = {
    '.txt': 'extract_text_from_txt',
    '.md': 'extract_text_from_txt',
    '.rst': 'extract_text_from_txt',
    '.docx': 'extract_text_from_docx',
    '.pdf': 'extract_text_from_pdf',
    '.png': 'extract_text_from_image',
    '.jpg': 'extract_text_from_image',
    '.jpeg': 'extract_text_from_image',
    '.bmp': 'extract_text_from_image',
    '.tiff': 'extract_text_from_image',
    '.tif': 'extract_text_from_image',
    '.wav': 'extract_text_from_audio',
    '.mp3': 'extract_text_from_audio',
    '.m4a': 'extract_text_from_audio',
    '.ogg': 'extract_text_from_audio',
    '.flac': 'extract_text_from_audio',
}

def extract_text_from_txt(file_path):
    """Extract text from plain text files."""
    try:
        with open(file_path, 'r', encoding="utf-8", errors='ignore') as f:
            return f.read()
    except Exception as e:
        logger.error(f"Error reading text file {file_path}: {e}")
        return f"[Error reading text file: {e}]"

def extract_text_from_docx(file_path):
    """Extract text from DOCX files."""
    try:
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        logger.error(f"Error reading DOCX file {file_path}: {e}")
        return f"[Error reading DOCX file: {e}]"

def extract_text_from_pdf(file_path):
    """Extract text from PDF files, using OCR if needed."""
    try:
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                page_text = page.extract_text()
                if page_text and page_text.strip():
                    text += f"\n--- Page {page_num} ---\n"
                    text += page_text
                else:
                    # Try OCR for scanned PDFs
                    try:
                        img = page.to_image(resolution=300).original
                        ocr_text = pytesseract.image_to_string(img)
                        if ocr_text.strip():
                            text += f"\n--- Page {page_num} (OCR) ---\n"
                            text += ocr_text
                    except Exception as ocr_error:
                        text += f"\n--- Page {page_num} [OCR Error: {ocr_error}] ---\n"
        return text
    except Exception as e:
        logger.error(f"Error reading PDF file {file_path}: {e}")
        return f"[Error reading PDF file: {e}]"

def extract_text_from_image(file_path):
    """Extract text from image files using OCR."""
    try:
        return pytesseract.image_to_string(Image.open(file_path))
    except Exception as e:
        logger.error(f"Error reading image file {file_path}: {e}")
        return f"[Error reading image file: {e}]"

def extract_text_from_audio(file_path):
    """Extract text from audio files using speech recognition."""
    try:
        recognizer = sr.Recognizer()
        
        # Convert audio to WAV format if needed
        if not file_path.lower().endswith('.wav'):
            audio = AudioSegment.from_file(file_path)
            with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_wav:
                audio.export(temp_wav.name, format='wav')
                file_path = temp_wav.name
        
        with sr.AudioFile(file_path) as source:
            audio_data = recognizer.record(source)
            try:
                return recognizer.recognize_google(audio_data)
            except sr.UnknownValueError:
                return "[Unrecognized Speech]"
            except sr.RequestError as e:
                return f"[API Request Error: {e}]"
    except Exception as e:
        logger.error(f"Error reading audio file {file_path}: {e}")
        return f"[Error reading audio file: {e}]"

def process_folder(folder_path, output_file):
    """Process all supported files in a folder and its subfolders."""
    if not os.path.exists(folder_path):
        logger.error(f"Folder does not exist: {folder_path}")
        return False

    processed_files = 0
    total_files = 0
    
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write(f"Text Extraction Report\n")
        out.write(f"=====================\n")
        out.write(f"Source Folder: {folder_path}\n")
        out.write(f"Generated on: {os.path.basename(output_file)}\n")
        out.write(f"{'='*50}\n\n")
        
        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                ext = Path(file_path).suffix.lower()
                
                if ext in FILE_HANDLERS:
                    total_files += 1
                    logger.info(f"Processing {file_path}...")
                    
                    try:
                        handler_name = FILE_HANDLERS[ext]
                        handler = globals()[handler_name]
                        text = handler(file_path)
                        
                        out.write(f"\n{'='*50}\n")
                        out.write(f"FILE: {file_path}\n")
                        out.write(f"TYPE: {ext.upper()} file\n")
                        out.write(f"SIZE: {os.path.getsize(file_path)} bytes\n")
                        out.write(f"{'='*50}\n")
                        out.write(text)
                        out.write("\n")
                        
                        processed_files += 1
                        logger.info(f"Successfully processed {file_path}")
                        
                    except Exception as e:
                        logger.error(f"Failed to process {file_path}: {e}")
                        out.write(f"\n{'='*50}\n")
                        out.write(f"FILE: {file_path}\n")
                        out.write(f"ERROR: {e}\n")
                        out.write(f"{'='*50}\n")
    
    logger.info(f"Processing complete. {processed_files}/{total_files} files processed successfully.")
    return True

def main():
    """Main entry point for the script."""
    if len(sys.argv) != 3:
        print("Usage: python extract_folder_text.py <folder_path> <output_file.txt>")
        print("Example: python extract_folder_text.py ./documents ./output.txt")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    output_file = sys.argv[2]
    
    logger.info(f"Starting text extraction from {folder_path} to {output_file}")
    
    if process_folder(folder_path, output_file):
        print(f"✅ Text extraction complete! Check {output_file}")
    else:
        print("❌ Text extraction failed. Check logs for details.")
        sys.exit(1)

if __name__ == "__main__":
    main()
