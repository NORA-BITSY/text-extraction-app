#!/usr/bin/env python3
"""
Example usage script for the text extraction application.
This script demonstrates how to use the extract_folder_text.py module programmatically.
"""

import os
import tempfile
import shutil
from pathlib import Path
from extract_folder_text import process_folder, FILE_TYPES

def create_sample_files(sample_dir):
    """Create sample files for testing the extraction functionality."""
    
    # Create sample text file
    with open(os.path.join(sample_dir, "sample.txt"), "w") as f:
        f.write("This is a sample text file.\nIt contains multiple lines of text.\n")
    
    # Create sample markdown file
    with open(os.path.join(sample_dir, "sample.md"), "w") as f:
        f.write("# Sample Markdown\n\nThis is a **markdown** file with formatting.\n\n- Item 1\n- Item 2\n")
    
    # Create subdirectory with more files
    sub_dir = os.path.join(sample_dir, "subfolder")
    os.makedirs(sub_dir, exist_ok=True)
    
    with open(os.path.join(sub_dir, "another.txt"), "w") as f:
        f.write("This file is in a subdirectory.\nIt will also be processed.\n")
    
    print(f"Created sample files in: {sample_dir}")
    return sample_dir

def demonstrate_usage():
    """Demonstrate the usage of the text extraction application."""
    
    # Create temporary directory for sample files
    with tempfile.TemporaryDirectory() as temp_dir:
        sample_dir = create_sample_files(temp_dir)
        
        # Define output file
        output_file = os.path.join(temp_dir, "extracted_text.txt")
        
        print("\n" + "="*50)
        print("TEXT EXTRACTION DEMO")
        print("="*50)
        print(f"Processing folder: {sample_dir}")
        print(f"Output file: {output_file}")
        print("-"*50)
        
        # Process the folder
        process_folder(sample_dir, output_file)
        
        # Display results
        if os.path.exists(output_file):
            print("\nExtraction completed successfully!")
            print("\nExtracted content preview:")
            print("-"*30)
            with open(output_file, 'r') as f:
                content = f.read()
                print(content[:500] + "..." if len(content) > 500 else content)
        else:
            print("Error: Output file was not created")

def show_supported_formats():
    """Display all supported file formats."""
    print("\n" + "="*50)
    print("SUPPORTED FILE FORMATS")
    print("="*50)
    
    categories = {
        "Text Documents": ['.txt', '.md', '.markdown', '.rst'],
        "Office Documents": ['.docx'],
        "PDFs": ['.pdf'],
        "Images": ['.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.tif', '.gif'],
        "Audio Files": ['.wav', '.mp3', '.m4a', '.ogg', '.flac', '.aac']
    }
    
    for category, extensions in categories.items():
        print(f"\n{category}:")
        for ext in extensions:
            print(f"  - {ext}")
    
    print(f"\nTotal supported formats: {len(FILE_TYPES)}")

if __name__ == "__main__":
    print("Text Extraction Application - Example Usage")
    print("="*50)
    
    # Show supported formats
    show_supported_formats()
    
    # Run demonstration
    demonstrate_usage()
    
    print("\n" + "="*50)
    print("Demo completed!")
    print("To use with your own files:")
    print("python extract_folder_text.py <folder_path> <output_file.txt>")
