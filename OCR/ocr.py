import pytesseract
import PIL.Image
import cv2
from pytesseract import Output


"""
--psm: This option sets the Page Segmentation Mode (PSM) to one of the following values:
0: OCR engine will attempt to detect the layout of the document and treat it as a single text block.
1: Treat the image as a single text line.
2: Treat the image as a single word.
3: Treat the image as a single word in a circular area.
4: Treat the image as a single character.
6: Treat the image as a single text line, bypassing hacks that are dependent on the layout of the image.
7: Treat the image as a single text line, assuming that it is a SAR (Simple Automated Reading) machine-printed text.
8: Treat the image as a single character, bypassing hacks that are dependent on the layout of the image.
9: Treat the image as a single text block, bypassing hacks that are dependent on the layout of the image.
10: Treat the image as a single text block, assuming that it is a formatted document.
11: Treat the image as a single text block, but allow for the detection of text in multiple columns.
12: Treat the image as a single text block, assuming that it is a low-resolution image.
13: Treat the image as a single text block, assuming that it is a printed or synthetic image.

"""

"""
--oem: This option sets the OCR Engine Mode (OEM) to one of the following values:
0: Tesseract will use the legacy engine.
1: Tesseract will use the neural network engine.
2: Tesseract will use the LSTM engine.
3: Tesseract will use the OCR engine optimized for the language specified by the --lang option.

"""

myconfig = r"--psm 6 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("street.jpg"), config=myconfig)
print(text)

img = cv2.imread('street.jpg')
height, width, _ = img.shape

data = pytesseract.image_to_data(img,config=myconfig,output_type=Output.DICT)

amount_boxes = len(data['text'])

for i in range(amount_boxes):
    if float(data['conf'][i]) > 40:
        (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        img = cv2.putText(img,data['text'][i],(x,y+h+20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(232, 235, 52),2,cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey(0)