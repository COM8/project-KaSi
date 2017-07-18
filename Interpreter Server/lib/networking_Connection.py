import socket
from Interpreter.main import Interpreter


class networking_Connection:
    def __init__(self, theLog):
        self.__networkLog = theLog
        self.__clientIP = ""
        self.__aktiv = True

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(("", 50000))
            self.serverIP = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
            s.close()
        except OSError or socket.error:
            self.__networkLog.printError("the systen has no ip the server is going to halt now")
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
            self.__aktiv = True
            theInterpreter = Interpreter()
            self.__networkLog.printMessage("starting server")
            while self.__aktiv:
                try:
                    komm, addr = s.accept()
                except OSError or socket.error:
                    self.deaktivateServer()
                    komm.close()
                    s.close()
                    self.__networkLog.printError("unable to accept kommunikation terminating")
                    break
                while True:
                    try:
                        data = komm.recv(4096)
                    except OSError or socket.error:
                        break
                    if not data:
                        theMessage = ""
                        komm.close()
                        break
                    theMessage = data.decode()
                    theAnswer = str(theInterpreter.newOrder(str(theMessage)))
                    if not theAnswer == "success":
                        if not theAnswer == "stopServer":
                            print(theAnswer)
                        else:
                            komm.send("server stopped by client".encode())
                            self.__networkLog.printWarning("server stopped by client")
                            self.deaktivateServer
                            s.close
                            komm.close
                            return
                    self.__networkLog.printMessage("client sended: "+theMessage+"; result: "+theAnswer)
                    komm.send(theAnswer.encode())
                    theAnswer = ""
            s.close()
        except KeyboardInterrupt:
            self.__networkLog.printMessage("server Stopped with keyboard interrupt")
        except Exception as e:
            self.__networkLog.printError("unknown Error: "+str(e))
