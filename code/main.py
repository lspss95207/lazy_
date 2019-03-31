from face_tracking import *
from servo import *
from launcher_control import *
from mcs import *

#----facial_recognition setup----

resolution = (320,240)
bound = ( resolution[0]*(0.5-0.1) , resolution[0]*(0.5+0.1) )


#----face tracking module----
track = face_track(resolution)

#----launcher control module----
food_launcher = launcher(4,5,6)


while True:

    if(cloud_to_local("Power") == "0"):                         #If power switch on MCS is off, exit the program
        break


    food_launcher.scan_rotate(5)                                #rotate the base to scan for faces

    loc = track.face_loc()                                      #scan for faces



    if(loc[0][0] == -1):                                        #No face has been found

        print "No Face"
        local_to_cloud("no_face","face")                            #send data to MCS
        continue;

    elif(loc[0][0] > bound[0] and loc[0][0] < bound[1]):        #Check if the face is inside center boundary

        print "center"
        local_to_cloud("center","face")                             #send data to mcs

        if(loc[0][1] > 200 and loc[1] < 50):                        #calculate the firing angle 
            angle = 45
        else:                                               
            angle = 1550/loc[1]+(loc[0][1]-resolution[1]/2)/12



        track.capture()                                             #capture the picture of the face 

        food_launcher.fire_food(3,angle)                            #fire food

    else:                                                       #Check if the face has been found but not in center boundary
        print "not center"          
        local_to_cloud("not_center","face")                         #send data to MCS
        
   







