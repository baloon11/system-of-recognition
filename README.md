Python-script (the basis for system of recognition)

This small script: 
- takes an image file (test.png),
- cuts the desired part and stores it in a temporary file (tmp_pic.jpg)
- Then letters and numbers from this temporary file are recognized 
  and data stored in the file (out.txt)

This is a basic script based on which you can build a more sophisticated recognition system.

Usage
-----
python ocr_task.py


Requirements
------------
##OCR Tesseract – Text Recognition
	sudo apt-get install tesseract-ocr
        and
	Install a language file:
	sudo apt-get install tesseract-ocr-eng

See more details:
http://ubuntu.flowconsult.at/linux/ocr-tesseract-text-recognition-ubuntu-14-04/

##Pytesseract
	pip install Pillow==2.9.0
	pip install pytesseract==0.1.6

See more details how to install:
http://www.quora.com/How-do-I-use-PyTesser-and-Tesseract-OCR-in-Ubuntu-with-Python

---------------------------------------

A short video, how this script works:

https://www.youtube.com/watch?v=2GTQeUvkvwo



