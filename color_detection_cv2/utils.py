import cv2 as cv
import numpy as np


def get_bounds(color):
    c = np.uint8([[color]])

    # print(c)

    hscC = cv.cvtColor(c, cv.COLOR_BGR2HSV)

    # print(hscC)

    lower_limit = hscC[0][0][0] - 10, 100, 100
    upper_limit = hscC[0][0][0] + 10, 255, 255

    # print(lower_limit)
    # print(upper_limit)

    lower_limit = np.array(lower_limit, dtype=np.uint8)
    upper_limit = np.array(upper_limit, dtype=np.uint8)

    # print(lower_limit)
    # print(upper_limit)

    return lower_limit, upper_limit


# get_bounds([0, 255, 255])
