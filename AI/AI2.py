from PIL import Image
import pytesseract
import os

path = "AI/media/test2.png"
config = r"--psm 11 --oem 3 -l spa"

print(pytesseract.image_to_string(Image.open(path), config=config))