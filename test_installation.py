#!/usr/bin/env python3
"""
Test script to verify the installation and basic functionality of the text extraction application.
"""

import sys
import subprocess
import importlib.util

def check_python_version():
    """Check if Python version is 3.7 or higher."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7 or higher is required")
        return False
    print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
    return True

def check_package(package_name):
    """Check if a package is installed."""
    spec = importlib.util.find_spec(package_name)
    if spec is None:
        print(f"❌ {package_name} is not installed")
        return False
    print(f"✅ {package_name} is installed")
    return True

def check_tesseract():
    """Check if Tesseract OCR is available."""
    try:
        import pytesseract
        pytesseract.get_tesseract_version()
        print("✅ Tesseract OCR is available")
        return True
    except Exception as e:
        print(f"❌ Tesseract OCR not found: {e}")
        print("   Please install Tesseract OCR:")
        print("   - Windows: https://github.com/UB-Mannheim/tesseract/wiki")
        print("   - macOS: brew install tesseract")
        print("   - Linux: sudo apt-get install tesseract-ocr")
        return False

def main():
    """Run all installation checks."""
    print("Text Extraction Application - Installation Check")
    print("=" * 50)
    
    checks = [
        ("Python Version", check_python_version),
        ("pytesseract", lambda: check_package("pytesseract")),
        ("PIL (Pillow)", lambda: check_package("PIL")),
        ("pdfplumber", lambda: check_package("pdfplumber")),
        ("python-docx", lambda: check_package("docx")),
        ("SpeechRecognition", lambda: check_package("speech_recognition")),
        ("Tesseract OCR", check_tesseract),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\nChecking {name}...")
        results.append(check_func())
    
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print("🎉 All checks passed! The application is ready to use.")
        print("\nUsage:")
        print("python extract_folder_text.py <folder_path> <output_file.txt>")
    else:
        print(f"⚠️  {total - passed} out of {total} checks failed.")
        print("Please install the missing dependencies and try again.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
