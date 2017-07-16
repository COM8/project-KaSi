#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform
from lib.log import log
from lib.networking_Connection import networking_Connection


def manageMessage():
    network.loop()


def initProgramm():
    mainLog.printMessage("beginn Init")
    message = "ip-adress: " + network.returnserverIP()
    mainLog.printMessage(message)
    theOs = platform.system()
    currentOs = "OS: " + theOs
    mainLog.printMessage(currentOs)
    if theOs == "Windows":
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("KiliTec.Projekt_KaSi_Server.1,0")
        ctypes.windll.kernel32.SetConsoleTitleA(b"Projekt KaSi Server")
    elif theOs == "Linux":
        pass
    else:
        mainLog.printWarning("os not supportet")
        mainLog.printWarning("system is going to halt now")
        exit()


# global variables
if __name__ == "__main__":
    global mainLog
    global network
    mainLog = log("Server.log", 1)
    mainLog.printMessage("starting server")
    mainLog.printMessage("init network")
    network = networking_Connection(mainLog)
    if network.initSuccess:
        mainLog.printMessage("network init succesful")
    else:
        mainLog.printError("network couldn't be initialized")
        mainLog.printMessage("system is going to halt now")
        exit()
    initProgramm()
    network.loop()
    mainLog.printMessage("system is going to halt now")
