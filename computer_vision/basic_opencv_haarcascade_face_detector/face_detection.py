import cv2 as cv
def resize(img,scale):
    width=int(img.shape[1]*int(scale)/100)
    height=int(img.shape[0]*int(scale)/100)
    dim=(width,height)
    return cv.resize(img,dim,interpolation=cv.INTER_AREA)

img=cv.imread(r"D:\Lane Detector\photos\test_case\IMG_4074.jpg")
scale=input("Please input scale\n")
int(scale)
res=resize(img,scale)
gray=cv.cvtColor(res,cv.COLOR_BGR2GRAY)

har_cascade=cv.CascadeClassifier(r"D:\Lane Detector\har_face.xml")
face_rec=har_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=10)

print(f'faces fount {len(face_rec)}')
for (x,y,w,h) in face_rec:
    cv.rectangle(res,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    
cv.imshow("detect",res)
cv.waitKey(0)