from time import sleep
from Interpreter.lib.System import System
from Interpreter.lib.Raspberry import theGPIO
class Interpreter:
    """description of class"""
    isRaspberry=False
    def __init__(self):
        pass

    def __stopServer(self):
        if self.isRaspberry:
            GPIO.cleanup()


    def newOrder(self, theOrder):
        i = 0
        theLibary = ""
        theMethodewithAttribute = ""
        if theOrder=="isRaspberry":
            return self.finishOrder(self.isRaspberry)
        else:
            while theOrder[i] != '.':
                theLibary = theLibary + theOrder[i]
                i = i + 1
                if len(theOrder) == i:
                    return "Syntax Error"
            while i + 1 < len(theOrder):
                i = i + 1
                theMethodewithAttribute = theMethodewithAttribute + str(theOrder[i])
            return self.getMethode(theLibary, theMethodewithAttribute)

    def getMethode(self, theLibary, theMethodewhithAttribute):
        i = 0
        theMethode = ""
        theAttribute = ""
        while theMethodewhithAttribute[i] != '(':
            theMethode = theMethode + theMethodewhithAttribute[i]
            i = i + 1
            if len(theMethodewhithAttribute) == i:
                return "Syntax Error"
        while i < len(theMethodewhithAttribute):
            theAttribute = theAttribute + theMethodewhithAttribute[i]
            i = i + 1
        return self.getAttribute(theLibary, theMethode, theAttribute)
    def getAttribute(self, theLibary, theMethode, theAttributee):
        phase=0
        theAttribute = list()
        var=""
        for thechar in theAttributee:
            if thechar =='(' and phase==0:
                phase=1
            elif phase==1:
                if thechar == ';':
                    theAttribute.append(var)
                    var=""
                elif thechar!=')':
                    var = var+thechar
                else:
                    break
        theAttribute.append(var)
        return self.runOrder(theLibary,theMethode,theAttribute)

    def runOrder(self, theLibary, theMethode, theAttribute):
        if theLibary == "System":
            return self.libSystem(theMethode, theAttribute)
        elif theLibary=="Demo":
            return self.libDemo(theMethode,theAttribute)
        elif theLibary=="GPIO":
            return self.libGPIO(theMethode,theAttribute)
        else:
            return "Syntax Error"
    def libGPIO(self,theMethode,theAttribute):
        if self.isRaspberry:
            if theMethode=="setup":
                if len(theAttribute)==2:
                    return self.finishOrder(GPIO.theSetup(theAttribute[0],theAttribute[1]))
                else:
                    return "Syntax Error"
    def libDemo(self,theMethode,TheAttribute):
        if self.isRaspberry:
            from Interpreter.lib.Demo import demo
            libdemo=demo()
            if theMethode=="setRed":
                return self.finishOrder(libdemo.setRed())
            elif theMethode=="setGreen":
                return self.finishOrder(libdemo.setGreen())
            elif theMethode=="clr":
                return self.finishOrder(libdemo.clr())
            elif theMethode=="clrGreen":
                return self.finishOrder(libdemo.clrGreen())
            elif theMethode=="clrRed":
                return self.finishOrder(libdemo.clrRed())
        else:
            return("Error System is no Raspberry")
    def libSystem(self, theMethode, theAttribue):
        libSys = System()
        if theMethode == "writeLine":
            return  self.finishOrder(libSys.writeLine(str(theAttribue[0])))
        elif theMethode == "cmd":
            command=theAttribue.split()
            return self.finishOrder(libSys.writetoCmd(command))
        elif theMethode=="shutdown":
            return self.finishOrder(libSys.shutdown())
        elif theMethode=="lock":
            return self.finishOrder(libSys.lockPc())
        elif theMethode=="logout":
            return self.finishOrder(libSys.logOUT())
        elif theMethode=="stopServer":
            self.__stopServer()
            return "stopServer"
            #return self.finishOrder(libSys.die())
        else:
            return "Syntax Error"

    def finishOrder(self, theAnswer):
        return theAnswer
