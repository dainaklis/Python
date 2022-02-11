import cv2
import numpy
from tkinter import *
from tkinter.filedialog import *

qrImage = cv2.imread('E:\\DARBAI\\Phyton\\Mokymai\\QR\\vcard-QR.png')

cv2.imshow("QR Code", qrImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
