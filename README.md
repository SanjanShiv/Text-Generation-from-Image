# Text-Generation-from-Image
Transform images into descriptive text with our AI model. Perfect for alt-text, summaries, and more.
Introduction
This report documents the development of a Python program that extracts text and visual 
elements from an image, and then generates an HTML file with the extracted content. The 
program leverages Optical Character Recognition (OCR) and image processing techniques to 
achieve its objectives.
Approach
The main approach of the program is divided into three primary tasks:
1. Text Extraction: Using OCR to extract text from the image.
2. Visual Element Segmentation: Using image processing techniques to identify and 
extract visual elements from the image.
3. HTML Generation: Creating an HTML file that embeds the extracted text and visual 
elements.
Technologies Used
The program utilizes the following technologies and libraries:
• Python: The programming language used to develop the program.
• Tesseract OCR: An open-source OCR engine used to extract text from images.
• Pillow (PIL): A Python Imaging Library (PIL) fork used for opening and 
manipulating images.
• OpenCV: An open-source computer vision and machine learning software library 
used for image processing tasks.
• Base64: A module used to encode binary data (visual elements) as ASCII strings for 
embedding in HTML.
Implementation Details
Required Libraries
Before running the program, the following libraries need to be installed:
• Tesseract OCR: Download and install Tesseract OCR from
https://github.com/tesseract-ocr/tesseract.
• OpenCV: Install using pip:
pip install opencv-python
• Pillow: Install using pip:
pip install pillow
• Pytesseract: Install using pip:
pip install pytesseract
