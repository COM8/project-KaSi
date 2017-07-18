class theGPIO:

    def __init__(self):
        try:
            global theGPIO
            from RPi import GPIO as theGPIO
            self.__isRaspberry = True
            theGPIO.setmode(theGPIO.BCM)
            self.__isDeclared = dict()
            self.__theDirection = dict()
        except ImportError:
            self.__isRaspberry = False

    def theSetup(self, thePin, Direction):
        try:
            Pin = int(thePin)
        except ValueError:
            return "Error Pin is no Count"
        if self.__isRaspberry:
            try:
                if self.__isDeclared[Pin]:
                    pass
            except KeyError:
                self.__isDeclared[Pin] = True
                if Direction == "input":
                    theGPIO.setup(Pin, theGPIO.IN)
                    try:
                        if self.__theDirection[Pin] == "output":
                            self.__theDirection[Pin] = "input"
                    except KeyError:
                        self.__theDirection[Pin] = "output"
                    return "Success"
                elif Direction == "output":
                    try:
                        theGPIO.setup(Pin, theGPIO.OUT)
                        if self.__theDirection[Pin] == "input":
                            self.__theDirection[Pin] = "output"
                    except KeyError:
                        self.__theDirection[Pin] = "output"
                    return "Success"
                else:
                    return "unknown Direction"
            else:
                return "Error Server is no Raspberry"

    def theOutput(self, thePin, direction):
        try:
            Pin = int(thePin)
            Direction = int(direction)
        except ValueError:
            return "Error Pin is no Count"
        if self.__isRaspberry:
            try:
                if self.__isDeclared[Pin]:
                    if self.__theDirection[Pin] == "output":
                        theGPIO.output(Pin, Direction)
                        return "Success"
                    else:
                        return "Pin has to be declared as an Output"
            except KeyError:
                return "Error Pin has to be assigned before usage"
        else:
            return "Error Server is no Raspberry"

    def cleanup(self):
        if self.__isRaspberry:
            theGPIO.cleanup()
