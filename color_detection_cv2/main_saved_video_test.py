# %%
# from functools import update_wrapper
import os

import cv2
import numpy as np
import pandas as pd
from PIL import Image
from utils import get_bounds

# %%
# vid_path = os.path.join(".", "yellow_flower.mp4")
vid_path = os.path.join(".", "color_detection_cv2", "yellow_flower.mp4")
print(vid_path)
vid = cv2.VideoCapture(vid_path)
print(type(vid))
print(vid)


# %%
yellow = [0, 255, 255]  # bgr yellow
# white = [200, 200, 200]
lower_limit, upper_limit = get_bounds(yellow)
print(lower_limit)
print(upper_limit)


# %%
def bbox_draw(bbox, frame):
    x1, y1, x2, y2 = bbox
    frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
    return frame


# %% MASK CLEANING
def mask_clean(mask):
    kernel = np.ones((1, 1), np.uint8)
    clean = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    clean = cv2.morphologyEx(clean, cv2.MORPH_CLOSE, kernel)
    return clean


# %%   show the hsv frame + masking everything except the yelloww color
ret = True
while ret:
    ret, frame = vid.read()
    frame = cv2.resize(frame, (1050, 550))
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frame_hsv, lower_limit, upper_limit)
    mask = mask_clean(mask)
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(
        mask, connectivity=8
    )
    for i in range(1, num_labels):
        x1 = stats[i, cv2.CC_STAT_LEFT]
        y1 = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]

        if w >= 60 and h >= 60:
            bbox = (x1, y1, x1 + w, y1 + h)
            frame = bbox_draw(bbox, frame)
    # this part down gets all the flower as a one big yellow object
    # mask_ = Image.fromarray(mask)
    # print(mask)
    # print(mask_)
    # bbox = mask_.getbbox()
    # if bbox is not None:
    # frame = bbox_draw(bbox, frame)

    cv2.imshow("Frame", frame)
    # cv2.imshow("Frame hsv", frame_hsv)
    cv2.imshow("Mask img", mask)
    if cv2.waitKey(40) & 0xFF == ord("q"):
        break
vid.release()
cv2.destroyAllWindows()


# %%
