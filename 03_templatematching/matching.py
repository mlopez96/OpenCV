import numpy as np
import cv2
import time

#path = os.path.dirname(os.path.abspath('03_templatematching/assets'))
#os.chdir(path)

img = cv2.imread('assets/footballpractice.png',0)


template = cv2.imread('assets/football.png',0)
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

def wait_for_user_input():
    while True:
        user_input = input("Press any key for next method")
        if user_input:
            break
    time.sleep(1)


for method in methods:
    img2 = img.copy()
    wait_for_user_input()

    #Performs convolution, sides it across, to see if there is a match in each region
    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc



bottom_right = (location[0] + w, location[1] + h)
cv2.rectangle(img2, location, bottom_right, 255, 5)
cv2.imshow('Match', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

if __name__ == "__main__":
    wait_for_user_input()