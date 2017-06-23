import socket
from Interpreter.main import Interpreter
from lib.log import log

class networking_Connection:
    """description of class"""

    def __init__(self,theLog):
        self.__networkLog=theLog
        self.__clientIP = ""
        self.__aktiv = True

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(("", 50000))
            self.serverIP = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in
                        [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
            s.close()
        except OSError:
            self.__networkLog.printError("The Systen has no IP the Server is going to Halt now")
            exit()

    def returnclientIP(self):
        return str(self.__clientIP)

    def returnserverIP(self):
        return self.serverIP

    def initSuccess(self):
        return True

    def aktivateServer(self):
        self.__aktiv = True

    def deaktivateServer(self):
        self.__aktiv = False

    def loop(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(("", 50000))
            s.listen(1)
            self.__aktiv=True
            theInterpreter = Interpreter()
            self.__networkLog.printMessage("starting Server")
            while self.__aktiv:
                try:
                    komm, addr = s.accept()
                except OSError:
                    self.deaktivateServer()
                    komm.close()
                    s.close()
                    self.__networkLog.printError("unable to accept kommunikation terminating")
                    break
                while True:
                    try:
                        data = komm.recv(4096)
                    except:
                        break
                    if not data:
                        theMessage = ""
                        komm.close()
                        break
                    theMessage = data.decode()
                    theAnswer = str(theInterpreter.newOrder(str(theMessage)))
                    if not theAnswer=="Success":
                        if not theAnswer=="stopServer":
                            print(theAnswer)
                        else:
                            komm.send("Server stopped by Client".encode())
                            self.__networkLog.printWarning("Server stopped by Client")
                            self.deaktivateServer
                            break


                    self.__networkLog.printMessage("Client sended: "+theMessage+"; Result: "+theAnswer)
                    komm.send(theAnswer.encode())
                    theAnswer = ""
            s.close()
        except KeyboardInterrupt:
            self.__networkLog.printMessage("server Stopped with keyboard Interrupt")
        except Exception as e:
            self.__networkLog.printError("unknown Error: "+str(e))