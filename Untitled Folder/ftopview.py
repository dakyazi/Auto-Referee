import numpy as np
import cv2 as cv

drawing = False # true if mouse is pressed
src_x, src_y = -1,-1

src_list = []

def select_points_src(event,x,y,flags,param):
    global src_x, src_y, drawing
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        src_x, src_y = x,y
        cv.circle(src_copy,(x,y),5,(0,0,255),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False

src_path = r'D:\AutoRefProj\videos\top.png'

src = cv.imread(src_path, -1)
src_copy = src.copy()
cv.namedWindow('src', cv.WINDOW_NORMAL)
cv.setMouseCallback('src', select_points_src)

while(1):
    cv.imshow('src',src_copy)
    k = cv.waitKey(1) & 0xFF
    if k == ord('s'):
        print('save points')
        cv.circle(src_copy,(src_x,src_y),5,(0,255,0),-1)
        src_list.append([src_x,src_y])
        print("src points:")
        print(src_list)      
    elif k == 27:
        break
cv.destroyAllWindows()