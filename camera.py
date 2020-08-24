from picamera import PiCamera
from time import sleep

def piCam(w=200,h=100,x=0,y=0,fill=True):
    camera = PiCamera()
    camera.resolution = (w,h)
    camera.start_preview(fullscreen= fill,window=(x,y,w,h))
