'''
Created on Nov 2, 2017

@author: Mitra Modi
"I pledge my honor that I have abided by the Stevens Honor System" - Mitra Modi

CS 115B - Lab 9
'''
from cs5png import *
import random

def mult(c, n):
    """ 
        mult uses only a loop and addition
        to multiply c by the integer n
    """
    result = 0
    for x in range(n):
        result += c
    return result

def update(c,n):
    """ 
        update starts with z=0 and runs z = z**2 + c
        for a total of n times. It returns the final z.
    """
    z = 0
    while n > 0:
        z = z**2 +c
        n += -1
    return z

c = 0.42 + 0.2j 
def inMSet(c,n):
    """ 
        inMSet takes in
        c for the update step of z = z**2+c
        n, the maximum number of times to run that step
        Then, it should return
        False as soon as abs(z) gets larger than 2
        True if abs(z) never gets larger than 2 (for n iterations)
    """
    z = 0
    t = 0
    while n > 0:
        t += 1
        z = z**2 +c
        n += -1 
        if abs(z) > 2:
            return t
    return 0


def weWantThisPixel( col, row ):
    """ 
        a function that returns True if we want
        the pixel at col, row and False otherwise
    """
    if col%10 == 0 and row%10 == 0:
        return True
    else:
        return False
def test():
    """ 
        a function to demonstrate how
        to create and save a png image
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    
    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()

"""Changing and to or in the weWantThisPixel function will make the image produce a grid instead of an image of dots"""


def scale(pix, pixMax, floatMin, floatMax):
    """ 
        scale takes in
        pix, the CURRENT pixel column (or row)
        pixMax, the total # of pixel columns
        floatMin, the min floating-point value
        floatMax, the max floating-point value
        scale returns the floating-point value that
        corresponds to pix
    """
    distance = floatMax - floatMin
    percent = (1.0*pix)/pixMax
    return percent*distance + floatMin

def mset():
    """ 
    creates a 300x200 image of the Mandelbrot set
    """
    width = 2100
    height = 1400
    image = PNGImage(width, height)
    NUMITER = 25
    XMIN = -2.0
    XMAX = 1.0
    YMIN = -1.0
    YMAX = 1.0
    for col in range(width):
        for row in range(height):
            x = scale(col, width, XMIN, XMAX)
            y = scale(row, height, YMIN, YMAX)
            c = x + y * 1j
            a = inMSet(c, NUMITER)
            image.plotPoint(col, row, (255*a/NUMITER,255*a/NUMITER,255*a/NUMITER))
    image.saveFile()

mset()