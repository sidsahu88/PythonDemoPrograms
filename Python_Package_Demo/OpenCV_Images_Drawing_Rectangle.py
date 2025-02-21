import cv2
import numpy as np

# True while Mouse button down, False while Mouse button up
drawing = False
ix = -1
iy = -1


def draw_rectangle(event, x, y, flags, param):
    global drawing, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)


cv2.namedWindow(winname="myrectangle")
cv2.setMouseCallback('myrectangle', draw_rectangle)

img = np.zeros((512, 512, 3))

while True:
    cv2.imshow('myrectangle', img)

    # Check if user pressed ESC key
    if cv2.waitKey(1) & 0xff == 27:
        break

cv2.destroyAllWindows()
