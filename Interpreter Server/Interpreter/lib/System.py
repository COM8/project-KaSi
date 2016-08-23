import platform
import subprocess
import os.path


class System(object):
    """description of class"""
    __theOS = ""

    def __init__(self):
        __theOS = platform.system()

    def writeLine(self, stringText):
        print(stringText)
        return "Success"

    def executeFile(self, direction):
        correctDirection = self.correctPath(direction)
        if os.path.exists(correctDirection):
            return self.runFile(correctDirection)
        else:
            return ("Error 404 file not Found")
        self.getEnding(direction)

    def runFile(self, direction):
        pass

    def stopServer(self):
        from os import sys
        sys.exit(0)
    def lockPc(self):
        try:
            import ctypes
            ctypes.windll.user32.LockWorkStation()
            return "Success"
        except:
            return "Error"
    def correctPath(self, direction):
        correctDirection = ""
        if self.__theOS == "Windows":
            sign = '\\'
        else:
            sign = '/'
        for theLetter in direction:
            if theLetter == "\\" or theLetter == "/":
                correctDirection = correctDirection + sign
            else:
                correctDirection = correctDirection + theLetter
        return correctDirection

    def theTruth(self):
        return (True)

    def writetoCmd(self, stringOrder):
        #return subprocess.getstatusoutput(stringOrder)
        return (os.popen(stringOrder).read())

    def shutdown(self):
        if self.__theOS == "Windows":
            return self.writetoCmd("shutdown -s -t 3000")
        else:
            return self.writetoCmd("shutdown -h 0")

    def systemInfo(self):
        theInfo = ""
        return theInfo

    def logOUT(self):
        self.writetoCmd("shutdown -l")
    def getEnding(self, direciton):
        ending = ""
        for i in reversed(direciton):
            ending = i + ending
            if i == ".":
                return (ending)
        return ("Can't specify the File Type")
