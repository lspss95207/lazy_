from mcs import *
from time import sleep
import os

while True:
    if(cloud_to_local("Power") == "1"):     #execute main.py when power switch on MCS is on
        os.system("python2 main.py")
        sleep(0.1)


