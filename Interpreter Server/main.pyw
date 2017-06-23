#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform
from lib.log import log
from lib.networking_Connection import networking_Connection


def manageMessage():
    network.loop()


def initProgramm():
    mainLog.printMessage("Beginn Init")
    message = "IP-Adress: " + network.returnserverIP()
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
        mainLog.printWarning("OS not Supportet")
        mainLog.printWarning("System is going to halt now")
        exit()


# global variables
if __name__=="__main__":
    global mainLog
    global network
    mainLog = log("Server.log", 1)
    mainLog.printMessage("Starte Server")
    mainLog.printMessage("init Network")
    network = networking_Connection(mainLog)
    if network.initSuccess:
        mainLog.printMessage("Network init succesful")
    else:
        mainLog.printError("Network couldn't be initialized")
        mainLog.printMessage("System is going to Halt now")
        exit()
    initProgramm()
    network.loop()
    mainLog.printMessage("System is going to Halt now")

