import cv2


picture = cv2.imread("image.jpg")

greypicture = cv2.cvtColor(picture,cv2.COLOR_BGR2GRAY)


haar_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face_rect = haar_cascade.detectMultiScale(greypicture,1.01,9)
#dontunderstandfullhaarcascasedetetmultiscale
print(face_rect)

for (x,y,w,h) in face_rect:
    cv2.rectangle(picture,(x,y),(x+w,y+h),(0,0,255),2)


cv2.imshow("face",picture)
cv2.waitKey(0)