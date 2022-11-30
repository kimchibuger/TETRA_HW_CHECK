#readline_test.py

import time
#import numpy as np
import cv2
from PIL import Image

path = './home/firefly/Downloads/blackout.png'

while True:
  try: 

    f = open("/sys/bus/iio/devices/iio:device0/in_voltage3_raw",'r')
    #f = open("/sys/bus/iio/devices/iio:device0/in_voltage4_raw",'r')

    
    line = f.readline()
    
    line = line.strip()  # line change remove
    
    #print(line)
    #print("sensor Data :",line)
    
    if line == '4095':
      print("=======================================")
      print("motion detected :",line)
      print("=======================================")
      #image = Image.open(path)
      #image.show()
      
      #img1 = np.zeros((512,512,3), np.uint8)
      #img2 - np.zeros((512,512), np.uint8)
      
      #cv2.imshow('img1',img1)
      #cv2.imshow('img2',img2)
      
      #cv2.waitkey
      
      #f.close
      #break;
    else:
      print("sensor Data :",line)
      
     
    f.close
    time.sleep(0.5)

    
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print ("motion ended!..\nExiting.")
    break;
  
   

        
