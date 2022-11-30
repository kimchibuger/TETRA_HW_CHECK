import serial
import time
import pynmea2

port = "/dev/ttyUSB0"

def parseGPS(res):   # GPS Sensor Data Parsing..
   
    res_decode = res.decode()
    res = str(res)
    print("raw Data :" ,res)
        
    
    if res_decode.find('RMC') > 0:
        
        print("=========================================================================================================")
        print ("------------------------------------------Parsing GPRMC-------------------------------------------------") 

        sdata = res.split(",")
        
        if sdata[2] == 'V':
           print ("no satellite data available")
           #return
                    
        time = sdata[1][0:2] + ":" + sdata[1][2:4] + ":" + sdata[1][4:6]
        lat = sdata[3] #latitude
        dirLat = sdata[4]      #latitude direction N/S
        lon = sdata[5] #longitute
        dirLon = sdata[6]      #longitude direction E/W
        speed = sdata[7]       #Speed in knots
        trCourse = sdata[8]    #True course
        date = sdata[9][0:2] + "/" + sdata[9][2:4] + "/" + sdata[9][4:6]  #date

        #print("Latitude : %s, Longitude : %s" % (lat,lon))
        print("---------------------------------------------------------------------------------------------------------")
        print ("time : %s, latitude : %s(%s), longitude : %s(%s), speed : %s, True Course : %s, Date : %s" %                     
        (time,lat,dirLat,lon,dirLon,speed,trCourse,date))
        print("---------------------------------------------------------------------------------------------------------")
        print("=========================================================================================================")
        

def decode(coord):
    #Converts DDDMM.MMMMM > DD deg MM.MMMMM min
    x = coord.split(".")
    head = x[0]
    tail = x[1]
    deg = head[0:-2]
    min = head[-2:]
    return deg + " deg " + min + "." + tail + " min"


print ("Receiving GPS data Start..")
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)

while True:

  try:
    res = ser.readline()
    parseGPS(res)
    #time.sleep(0.3)
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print ("Receiving GPS data Stop..\nExiting.")
    break;
  
   
ser.close()    
   
   
