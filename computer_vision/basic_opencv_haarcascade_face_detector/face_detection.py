import cv2 as cv

#to resize the image i have made a function
#to make the computer know how much it has to resize the image i have used .shape[1] and shape[0]
def resize(img,scale):
    width=int(img.shape[1]*int(scale)/100) #shape(x,y) is a pre defined methode which is used for the dimensions of any image basically .shape[0] means x-axis
    height=int(img.shape[0]*int(scale)/100) #shape(x,y) is a pre defined methode which is used for the dimensions of any image basically .shape[1] means y-axis
    dim=(width,height)
    return cv.resize(img,dim,interpolation=cv.INTER_AREA)

img=cv.imread(r"D:\Lane Detector\photos\test_case\IMG_4074.jpg")
scale=input("Please input scale\n")
int(scale)
res=resize(img,scale) #using resize function
gray=cv.cvtColor(res,cv.COLOR_BGR2GRAY)

#haarCascade is an algorithm which is used to to detect human or living beings based on the classifier type which you are using
#here I am using HaarCascade_face_default.xml file you can download it from google and save it in your computer

har_cascade=cv.CascadeClassifier(r"D:\Lane Detector\har_face.xml")#har_cascade is the local variable in which i am going to save the xml file of the haarFaceclassifier
face_rec=har_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=10)

print(f'faces found : {len(face_rec)}')

#this code is to mark all the faces by making green highleted hollow rectangle on the face
for (x,y,w,h) in face_rec:
    cv.rectangle(res,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    
cv.imshow("detect",res)
cv.waitKey(0)
