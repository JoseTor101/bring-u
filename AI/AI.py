import pytesseract
from pytesseract import Output
import PIL.Image
import cv2
import os

config = r"--psm 11 --oem 3 -l spa"

actualPath = os.path.dirname(os.path.abspath(__file__))
#parentPath = os.path.dirname(actualPath)
mediaPath = os.path.dirname(actualPath) + "\media" + "\AI"

print("MEDIA PATH: " + mediaPath)

imageName = input("Enter image name (Include the extension): ")
if imageName == "":
    # Use default image
    imageName = "test.png"

path = os.path.join(mediaPath, imageName)

img = cv2.imread(path)
height, width, _ = img.shape

data = pytesseract.image_to_data(img, config=config, output_type=Output.DICT)
boxes = pytesseract.image_to_boxes(img, config=config)

for i in range(len(data['text'])):
    print(data['text'][i])

for box in boxes.splitlines():
    box = box.split(" ")
    img = cv2.rectangle(img, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0,0,255), 1)

amount_boxes = len(data['text'])
for i in range(amount_boxes):
    if float(data['conf'][i]) > 60:
        (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)
        img = cv2.putText(img, data['text'][i], (x, y+height+10), cv2.FONT_HERSHEY_PLAIN, 0.7, (255, 0, 0), 1, cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey(0)

text = pytesseract.image_to_string(PIL.Image.open(path), config=config)
print("TEXT: " + text)