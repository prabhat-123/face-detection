import cv2 as cv
# Create a cascade classifier object
face_cascade = cv.CascadeClassifier("C:/Users/ASUS/Anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
img = cv.imread("E:/deeplearning/face_and_motion_detection/images/hello.jpg")
resizeimg = cv.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
#Converting the image into grayscale image
gray_img = cv.cvtColor(resizeimg,cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.5,minNeighbors=10)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    img= cv.rectangle(resizeimg,(x,y),(x+w,y+h),(0,255,0),3)

cv.imshow("Gray",resizeimg)

cv.waitKey(1)
cv.destroyAllWindows()