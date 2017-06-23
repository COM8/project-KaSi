import socket
from time import sleep
from datetime import datetime

class client(object):
    def __init__(self, name, group, Address, log):
        self.__theName = name
        self.__theAddress = Address
        self.__theGroup = group
        self.theLog = log
        self.__ignore=False

    """def __init__(self, name, group, Address):
        self.theName = name
        self.__theAddress = Address
        self.__theGroup = group"""

    def CheckIP(self):
        try:
            with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
                pass
            return True
        except OSError:
            return False

    def tryConnection(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.01)
            s.connect((self.__theAddress, 50000))
            s.close()
            return True
        except socket.error or WindowsError :
            return False



    def sendOrder(self, theOrder):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            s.connect((self.__theAddress, 50000))
            s.send(theOrder.encode())
            self.theLog.printMessage("sending: " + theOrder + "@" + self.__theName + ": " + self.__theAddress)
            theMessage = ""
            s.settimeout(0.01)
            startTime=datetime.now()
            while (datetime.now()-startTime).seconds<=1:
                try:
                    theResponce=s.recv(4096).decode()
                    s.close()
                    if theResponce == "success":
                        return True
                    else:
                        self.theLog.printMessage(self.__theName + ": " + self.__theAddress + " client respondet " + theMessage)
                        return theResponce
                except socket.error or socket.timeout:
                    pass
            else:
                self.theLog.printError(self.__theName + ": " + self.__theAddress + " no responce client timed out")
                return "no server responce timeout error"
        except socket.error or OSError:
            s.close()
            self.theLog.printError(self.__theName + ": " + self.__theAddress + " client socket locked, ist the server on?")
            return False

    def getName(self):
        return self.__theName

    def getGroup(self):
        return self.__theGroup
    def setName(self,newName):
        self.__theName=newName
    def getAddress(self):
        return self.__theAddress
    def setAddress(self,newAddress):
        self.__theAddress=newAddress

    def getCID(self):
        return self.clientID
