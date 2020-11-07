import cv2

v=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier('resources/haarcascade_frontalface_default.xml')

while(True):
    a,img=v.read()
    g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    f=face_cascade.detectMultiScale(g,1.2,7)
    flag=0
    for(x,y,z,d) in f:
        cv2.rectangle(img,(x,y),(x+z,y+d),(255,0,0),2)
        flag=1
    if(flag==1):
        cv2.putText(img, "Face Found", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 200, 0), 2)
    else:
        cv2.putText(img, "Face Not Found", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 200, 0), 2)
    cv2.imshow("face_recognition",img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break