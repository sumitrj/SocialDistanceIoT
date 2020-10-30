import matplotlib.pyplot as plt
import cv2 
import imutils
import numpy as np
import os

cap = cv2.VideoCapture('./example.mp4')

def dist(i,j):
    return ( (i[0]-j[0])**2 + (i[1]-j[1])**2 )**0.5

def actuate(x,y):
    
    if(0<=x<=200):
        signal(1)
        
    if(200<=x<=200):
        signal(2)
   
    if(400<=x<=600):
        signal(3)
   
    if(600<=x<=800):
        signal(4)
    
def signal(x):
    return 0

def oneframe(ix):
    
    ret,frame = cap.read()
    #plt.imshow(frame)
    
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    
    image = frame
    (regions, _) = hog.detectMultiScale(image, winStride=(4, 4), padding=(4, 4), scale=1.05)
    
    hpts = [(i[0] + int(i[2]/2), i[1] + int(i[-1]/2) )  for i in regions]
    close = []
    far = []
    near = []
    dists = []
    
    for i in range(len(hpts)):
        for j in range(len(hpts)):
            if(hpts[i]!=hpts[j]):
                dists.append(dist(hpts[i],hpts[j]))
                if(dist(hpts[i],hpts[j])<100):
                    close.append(i)
                if(dist(hpts[i],hpts[j])>100 and dist(hpts[i],hpts[j])<400):
                    near.append(i)
                if(dist(hpts[i],hpts[j])>500):
                    far.append(i)
    
    close,near,far = np.unique(close),np.unique(near),np.unique(far)
    
    for i in range(len(regions)):
        (x,y,w,h) = regions[i] 
        if(i in close):
            cv2.rectangle(image, (x, y),  (x + w, y + h), (255, 0, 0), 2)
            continue
        if(i in near):
            cv2.rectangle(image, (x, y),  (x + w, y + h), (255, 255, 0), 2) 
            continue
        if(i in far):
            cv2.rectangle(image, (x, y),  (x + w, y + h), (0, 255, 0), 2) 
            continue
    plt.imshow(image)
    
    cv2.imwrite('OI'+str(ix)+'.jpg',image)
    
    return {'Close':close, 'Far':far, 'Near':near, 'Dists':dists}
    #return close, far, near, dists

def run(itera,nf):
    os.mkdir('Run'+str(itera))
    for i in range(nf):
        oneframe(i)
