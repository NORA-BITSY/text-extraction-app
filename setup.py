from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="text-extraction-app",
    version="1.0.0",
    author="Text Extraction Team",
    author_email="team@textextraction.com",
    description="A comprehensive text extraction tool for documents, PDFs, images, and audio files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/textextraction/text-extraction-app",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Text Processing",
        "Topic :: Office/Business",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Sound/Audio",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "text-extract=extract_folder_text:main",
        ],
    },
    keywords="text extraction, OCR, PDF, image, audio, speech-to-text",
    project_urls={
        "Bug Reports": "https://github.com/textextraction/text-extraction-app/issues",
        "Source": "https://github.com/textextraction/text-extraction-app",
    },
)
