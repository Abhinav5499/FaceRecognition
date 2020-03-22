import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("messi.jfif", 1)
cv2.waitKey(0)
grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(grey_image, scaleFactor=1.05, minNeighbors=5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + h, y + w), (255, 0, 0), 3)
    print(w,h)
resize = cv2.resize(img, (int(img.shape[1]*3), int(img.shape[0]*3)))
cv2.imshow("Messi", resize)
# cv2.imshow("Messi", img)
cv2.waitKey(0)

cv2.destroyAllWindows()
