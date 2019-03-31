from SimpleCV import *
from time import sleep
from mcs import *
import base64



class face_track():
    #----setup display and camera----
    def __init__(self,resolu):  
        self.resolu = resolu
        self.cam = Camera(prop_set={'width':resolu[0], 'height':resolu[1]})
        self.dis = Display(resolution=(resolu[0],resolu[1]))

        self.capture_index = 1


    #----get the coordinate of face----
    def face_loc(self,with_log = True):
        frame = self.cam.getImage()
        self.frame = frame

        faces = frame.findHaarFeatures('face')
        mouths = frame.findHaarFeatures('mouth')
    
    
        if faces:
            for face in faces:
                
                w=face.width()
                h=face.height()

                if(with_log):
                    print "Face at: " + str(face.coordinates())
                    print "x: "+str(w)+" y: "+str(h)

                    facelayer = DrawingLayer((frame.width,frame.height))
                    facebox_dim = (w,h)
                    facebox = facelayer.centeredRectangle(face.coordinates(),facebox_dim,color=(255,0,0),width=3)
                    frame.addDrawingLayer(facelayer)
                    frame.applyLayers()
                
                    #frame.save(self.dis)
                    
                    self.frame = frame


                return [face.coordinates(),w]
        else:
            if(with_log):
                #frame.save(self.dis)
                print "No faces detected."

            return [[-1,-1],-1]
    
    #---send picture to MCS---
    def capture(self):          
        filename = "./capture" + str(self.capture_index) + ".jpg"
        self.frame.save(filename)
        
        with open(filename, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        local_to_cloud(encoded_string,"photo")

        self.capture_index += 1

