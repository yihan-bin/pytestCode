import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import myutils
import argparse
from imutils import contours

import imutils

ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='path to inpute image')

ap.add_argument('-i','--image',required=True,help='path to inpute image')


FIRST_NUMBER={
    '3':'Amercian Express',
    '4':'Visa',
    '5':'MasterCard',
    "6":'Discover Card‘
}
def cv_show(name,img):
