from PIL import Image
import pytesseract
import os

path = os.path.join('media', 'test.png')
print(pytesseract.image_to_string(Image.open(path)))