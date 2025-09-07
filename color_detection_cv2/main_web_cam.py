# %%
from functools import update_wrapper

import cv2
import numpy as np
import pandas as pd
from PIL import Image
from utils import get_bounds

# %%
webcam = cv2.VideoCapture(0)
yellow = [0, 255, 255]  # bgr yellow
lower_limit, upper_limit = get_bounds(yellow)
print(lower_limit)
print(upper_limit)


# %%
def bbox_draw(bbox, frame):
    x1, y1, x2, y2 = bbox
    frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
    return frame


# %%   show the hsv frame + masking everything except the yelloww color
ret = True
while ret:
    ret, frame = webcam.read()
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frame_hsv, lower_limit, upper_limit)
    mask_ = Image.fromarray(mask)
    # print(mask)
    # print(mask_)
    bbox = mask_.getbbox()
    if bbox is not None:
        frame = bbox_draw(bbox, frame)
    cv2.imshow("Frame", frame)
    # cv2.imshow("Frame hsv", frame_hsv)
    cv2.imshow("Mask img", mask)
    if cv2.waitKey(40) & 0xFF == ord("q"):
        break
webcam.release()
cv2.destroyAllWindows()


# %%
