import RPi.GPIO as GPIO ## Import GPIO library
class demo:
    greenPort=19
    redPort=6
    def __init__(self):        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.greenPort, GPIO.OUT)
        GPIO.setup(self.redPort, GPIO.OUT)
    def setRed(self):
        GPIO.output(self.redPort,True)
        return("Success")
    def setGreen(self):
        GPIO.output(self.greenPort,True)
        return("Success")
    def clrRed(self):
        GPIO.output(self.redPort,False)
        return("Success")
    def clrGreen(self):
        GPIO.output(self.greenPort,False)
        return("Success")
    def clr(self):
        GPIO.cleanup()
        return("Success")