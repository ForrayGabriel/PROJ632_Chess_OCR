import cv2 
import pytesseract
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# This file is an attempt to open an image, apply some effects on it and use the tesseract librairy to get
# the text from the image


img = cv2.imread('test.jpg')

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 

gray = get_grayscale(img)
thresh = thresholding(gray)
opening = opening(gray)
canny = canny(gray)


# Adding custom options
custom_config = r'--oem 3 --psm 6'
print("Sans traitement")
print(pytesseract.image_to_string(img, config=custom_config))
print("Apres grayscling et thersolding")
print(pytesseract.image_to_string(thresh, config=custom_config))
"""print("Apres grayscling et opening")
print(pytesseract.image_to_string(opening, config=custom_config))"""
"""
print("Apres grayscling et canny")
print(pytesseract.image_to_string(canny, config=custom_config))"""

h, w, c = gray.shape
boxes = pytesseract.image_to_boxes(gray) 
for b in boxes.splitlines():
    b = b.split(' ')
    gray = cv2.rectangle(gray, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('img', gray)
cv2.waitKey(0)