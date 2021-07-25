# Python code to read image
import cv2

# reading the image that is inserted below
# this image is just a placeholder
img = cv2.imread("PeterGriffin.png", cv2.IMREAD_COLOR)

# this is going to display the image on the page named Face Recognition.
cv2.imshow("Face Recognition", img)

# if we wanted to add how long the image is going to appear, basically using 1 or 2 would be how long, in seconds
cv2.waitKey(0)
# very big prototype on what I want to accomplish for a family guy episode
# basically how many times peter griffin's face appears in the episode itself
# for my final, I'm going to be doing a fight between peter griffin and the chicken from Season 10.


cv2.destroyAllWindows()
