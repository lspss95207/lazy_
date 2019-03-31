from servo import *
from time import sleep
from mcs import *

class launcher:
    #---initiate launcher PIN data
    def __init__(self,base_PIN,cannon_PIN,trigger_PIN):
        self.__base = Servo()
        self.__cannon = Servo()
        
        self.__base_PIN = base_PIN
        self.__cannon_PIN = cannon_PIN
        self.__trigger_PIN = trigger_PIN
        
        self.__base.attach(base_PIN)
        self.__cannon.attach(cannon_PIN)
        GPIO.setup(self.__trigger_PIN,GPIO.OUT)

        self.__base.write(0)
        self.__cannon.write(0)
        GPIO.output(self.__trigger_PIN,GPIO.LOW)

        
        self.__direction = True


    #---scan motion for facial recognition
    def scan_rotate(self,r_angle):
        self.__base_angle = self.__base.read()
        
        if (self.__base_angle > 170 or self.__base_angle < 0):
            self.__direction = not self.__direction;

        if(self.__direction):
            self.__base_angle += r_angle
        else:
            self.__base_angle -= r_angle

        self.__base.write(self.__base_angle)
        local_to_cloud(self.__base_angle,"base_angle")

    #---fire the food---
    def fire_food(self,fire_time = 3,angle = 40):
        self.__fire_angle = angle

        local_to_cloud(self.__fire_angle,"fire_angle")
        local_to_cloud(1,"fire")

        self.__cannon.write(40)

        
        GPIO.output(self.__trigger_PIN,GPIO.HIGH)
        sleep(fire_time)
        GPIO.output(self.__trigger_PIN,GPIO.LOW)
        

        self.__fire_angle = 0
        self.__cannon.write(0)         
        local_to_cloud(self.__fire_angle,"fire_angle")
        local_to_cloud(0,"fire")

        sleep(2)
        return



