import cv2
import numpy as np


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (0, 255, 0), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 75, (255, 0, 0), -1)


cv2.namedWindow(winname="mycircle")
cv2.setMouseCallback('mycircle', draw_circle)

img = np.zeros((512, 512, 3))

while True:
    cv2.imshow('mycircle', img)

    if cv2.waitKey(10) & 0xff == 27:
        break

cv2.destroyAllWindows()
