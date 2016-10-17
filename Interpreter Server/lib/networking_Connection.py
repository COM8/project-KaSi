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
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 50000))
        s.listen(1)
        self.__aktiv=True
        theInterpreter = Interpreter()
        self.__networkLog.printMessage("starting Server")
        print("Server Aktiv")
        while self.__aktiv:
            try:
                komm, addr = s.accept()
            except :
                self.deaktivateServer()
                komm.close()
                s.close()
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
                # print(theMessage)
                # return str(data.decode())
                theAnswer = str(theInterpreter.newOrder(str(theMessage)))
                if not theAnswer=="Success":
                    if not theAnswer=="stopServer":
                        print(theAnswer)
                    else:
                        komm.send("Server stopped by Client".encode())
                        self.__networkLog.printMessage("Server stopped by Client")
                        return ""


                self.__networkLog.printMessage("Client sended: "+theMessage+"; Result: "+theAnswer)
                komm.send(theAnswer.encode())
                theAnswer = ""
                # print("[{}] {}".format(addr[0], data.decode()))
                # nachricht = input("Antwort: ")
                # komm.send(nachricht.encode())
