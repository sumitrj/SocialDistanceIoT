import RPi.GPIO as gpio
import time as Time
gpio.setmode(gpio.BCM)

def signal(x):
  if(x==1): 
    gpio.output(18, gpio.HIGH)
    gpio.output(18, gpio.LOW)
    Time.sleep(1)
    gpio.output(18, gpio.HIGH)

  if(x==2):
    gpio.output(23, gpio.HIGH)
    gpio.output(23, gpio.LOW)
    Time.sleep(1)
    gpio.output(23, gpio.HIGH)
  
  if(x==3):
    gpio.output(23, gpio.HIGH)
    gpio.output(23, gpio.LOW)
    Time.sleep(1)
    gpio.output(18, gpio.HIGH)

## FUNCTION TO PROCESS A SINGLE FRAME

def oneframe(ix):

 ret,frame = cap.read()
 #plt.imshow(frame)

 ## SVM BASED DETECTION OF PEDESTRAIN
 hog = cv2.HOGDescriptor()
 hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

 image = frame
 (regions, _) = hog.detectMultiScale(image, winStride=(4, 4), padding=(4, 4), scale=1.05)

 hpts = [(i[0] + int(i[2]/2), i[1] + int(i[-1]/2) ) for i in regions]
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

 ## FUNCTION TO DRAW BOUNDING BOXES
 for i in range(len(regions)):
   (x,y,w,h) = regions[i]
   if(i in close):
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    continue
   if(i in near):
     cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
     continue
   if(i in far):
     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
     continue
   plt.imshow(image)

 ## FUNCTION TO WRITE OUTPUT IMAGES
 cv2.imwrite('OI'+str(ix)+'.jpg',image)

 return {'Close':close, 'Far':far, 'Near':near, 'Dists':dists}
 
 ## FUNCTION TO ITERATE AND PROCESS EACH FRAME

def run(itera,nf):
 os.mkdir('Run'+str(itera))
 for i in range(nf):
  oneframe(i)
