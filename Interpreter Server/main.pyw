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
    print(message)
    mainLog.printMessage(message)
    theOs = platform.system()
    currentOs = "OS: " + theOs
    mainLog.printMessage(currentOs)
    if theOs == "Windows":
        print(theOs)
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("KiliTec.Projekt_KaSi_Server.1,0")
        ctypes.windll.kernel32.SetConsoleTitleA(b"Projekt KaSi Server")
    elif theOs == "Linux":
        print(theOs)
    else:
        print("The OS isn't supported!")
        mainLog.printWarning("OS not Supportet")
        mainLog.printWarning("System is going to halt now")
        print("System is going to halt now")
        exit()


# global variables
if __name__=="__main__":
    global mainLog
    global network
    mainLog = log("Server.log", 1)
    mainLog.printMessage("Starte Server")
    print("Starte Server")
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

