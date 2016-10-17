#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import platform
import threading
from collections import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from concurrent import futures
from lib.clients import client
from lib.groups import group
from lib.log import log
from os import cpu_count


class ProjektKaSi():
    mainLog = log("client.log", True)
    __theGrous = []
    __theClients = []
    __clientSelected = False
    __groupSelected = False
    selectedID = 0

    def __init__(self):
        self.mainLog.printMessage("Starte Client")
        print("Starte Client")
        self.initProgramm()
        self.readConfig()
        self.testConnection()
        __clientSelected = False
        __groupSelected = False

    def initProgramm(self):
        self.mainLog.printMessage("Beginn Init")
        theOs = platform.system()
        currentOs = "OS: " + theOs
        self.mainLog.printMessage(currentOs)
        if theOs == "Windows" or theOs == "Linux":
            print(theOs)
        else:
            print("The OS isn't supported!")
            self.mainLog.printWarning("OS not Supportet")
            self.mainLog.printWarning("System is going to halt now")
            print("System is going to halt now")
            exit()

    def configEditor(self):
        import editConfig
        self.__theGrous.clear()
        self.__theClients.clear()
        self.readConfig()

    def getClientAmount(self):
        return len(self.__theClients)

    def getGroupAmount(self):
        return len(self.__theGrous)

    def getClientName(self, cID):
        return self.__theClients[cID].getName()

    def getGroupName(self, gID):
        return self.__theGrous[gID].getGroupName()

    def selectClient(self, cID):
        self.__groupSelected = False
        self.__clientSelected = True
        self.selectedID = cID

    def selectGroup(self, gID):
        self.__groupSelected = True
        self.__clientSelected = False
        self.selectedID = gID

    def selectAll(self):
        self.__groupSelected = False
        self.__clientSelected = False

    def createFolder(self, directiory):
        from os import makedirs, path
        if not path.isdir(directiory):
            makedirs(directiory)

    def readConfig(self):
        global gID, gID
        if platform.system() == "Windows":
            try:
                theconfigFile = open('config\\clients.config', 'r')
            except:
                window = Tk()
                window.withdraw()
                self.createFolder("config\\")
                File = open('config\\clients.config', 'a')
                File.close()
                messagebox.showinfo(
                    "Missing config", "No config Found. Createt an empty one")
                window.destroy()
                return
        else:
            try:
                theconfigFile = open('config/clients.config', 'r')
            except:
                window = Tk()
                window.withdraw()
                self.createFolder("config/")
                File = open('config/clients.config', 'a')
                File.close()
                messagebox._show("Missing config",
                                 "No config Found. Created an empty one")
                window.destroy()
                return
        theConfig = theconfigFile.read().splitlines()
        theconfigFile.close()
        for line in theConfig:
            if line[0] != " ":
                gID = self.createGroup(line) - 1
            else:
                theName = ""
                theAdress = ""
                phase = 0
                for buchstabe in line:
                    if buchstabe != " " and phase == 0:
                        if buchstabe == ":":
                            phase = 1
                        else:
                            theName = theName + buchstabe
                    elif buchstabe != " " and phase == 1:
                        theAdress = theAdress + buchstabe
                self.addGroupClient(gID, theName, theAdress)

    def createGroup(self, groupName):
        self.__theGrous.append(group(groupName, len(self.__theGrous) + 1))
        return len(self.__theGrous)

    def addGroupClient(self, roupID, clientName, clientAddress):
        self.__theClients.append(client(clientName, len(
            self.__theGrous) - 1, clientAddress, self.mainLog))
        self.__theGrous[
            len(self.__theGrous) - 1].addClient(self.__theClients[len(self.__theClients) - 1])

    def testConnection(self):
        for theGroup in self.__theGrous:
            print(str("Testing " + theGroup.getGroupName() + " :"))
            theGroup.testClients()

    def doJob(self, theOrder):
        if self.__clientSelected:
            self.__theClients[self.selectedID].sendOrder(theOrder)
        elif self.__groupSelected:
            self.__theGrous[self.selectedID].doJOB(theOrder)
        else:
            for theGroup in self.__theGrous:
                theGroup.doJOB(theOrder)

    def consoleLoop(self):
        Zustand = True
        while Zustand:
            Zustand = self.waitOrder(FALSE, "")

    def waitOrder(self, givenString, inputText):
        if self.__clientSelected:
            if self.selectedID <= len(self.__theClients):
                theText = "You@" + \
                    self.__theClients[self.selectedID].getName() + ": "
            else:
                print("Error selected ID doesn't exist")
                theText = "You@All: "
                __clientSelected = False
        elif self.__groupSelected:
            if self.selectedID < len(self.__theGrous):
                theText = "You@" + \
                    self.__theGrous[self.selectedID].getGroupName() + ": "
            else:
                print("Error selected ID doesn't exist")
                theText = "You@All: "
                self.__groupSelected = False
        else:
            theText = "You@All: "
        print("")
        if not givenString:
            inputText = input(theText)
        else:
            print(theText + inputText)
        if len(inputText) >= 2:
            Check = inputText[0] + inputText[1]
            if Check == "sc":
                i = len(inputText) - 1
                ID = ""
                while i >= 0:
                    if " " == inputText[i]:
                        break
                    else:
                        ID = ID + str(inputText[i])
                        i = i - 1
                try:
                    self.selectClient(int(ID))
                except ValueError:
                    print("Entered ID not vaild")
            elif Check == "sg":
                i = len(inputText) - 1
                ID = ""
                while i >= 0:
                    if " " == inputText[i]:
                        break
                    else:
                        ID = ID + str(inputText[i])
                        i = i - 1
                try:
                    self.selectGroup(int(ID))
                except ValueError:
                    print("Entered ID not vaild")
            elif Check == "sa":
                self.selectAll()
            elif Check == "lc":
                i = 0
                while i <= (len(self.__theClients) - 1):
                    value = "Client[" + str(i) + "]: " + self.__theClients[i].getName() + "@" + self.__theClients[
                        i].getAddress()
                    print(value)
                    i = i + 1
            elif Check == "lg":
                i = 0
                while i <= (len(self.__theGrous) - 1):
                    value = "Group[" + str(i) + "]: " + \
                        self.__theGrous[i].getGroupName()
                    print(value)
                    i = i + 1
            elif Check == "in":
                return FALSE
            elif Check == "tc":
                self.testConnection()
            elif Check == "rc":
                self.configEditor()
            else:
                self.doJob(inputText)
        else:
            self.doJob(inputText)
        return True

    def getLog(self):
        return self.mainLog


# Tkinter methodes
def sendOrderArg(var):
    sendOrder()


def sendOrder():
    theInput = inputt.get()
    inputt.delete(0, END)
    if theInput == "" or theInput == " ":
        messagebox.showinfo("Info", "Input Field can't be empty")
    else:
        Kasi.waitOrder(True, theInput)


def optionsChanged(selectedOption):
    if theList[selectedOption] == -1:
        Kasi.selectAll()
    elif selectedOption[0] == "[":
        Kasi.selectGroup(theList[selectedOption])
    else:
        Kasi.selectClient(theList[selectedOption])


def positionItems():
    # First Row
    width = interface.winfo_width()
    height = interface.winfo_height()
    wPercent = interface.winfo_width() / 100
    hPercent = interface.winfo_height() / 100
    # theHeight = 50
    wDistance = 0.3 * wPercent
    hDistance = 0.3 * hPercent
    theHeight = 24
    selectMenu.place(x=wDistance, y=hDistance,
                     width=wPercent * 15, height=theHeight)
    inputt.place(x=2 * wDistance + wPercent * 15, y=hDistance,
                 width=wPercent * 75 - wDistance, height=theHeight)
    button_Send.place(x=wPercent * 90 + 2 * wDistance, y=hDistance, width=wPercent * 10 - 3 * wDistance,
                      height=theHeight)
    # Last Row
    button_Quit.place(x=wPercent * 91 + wDistance, y=height - (hPercent * 0.05 + theHeight) - hDistance,
                      width=wPercent * 9 - 2 * wDistance, height=theHeight)
    button_ConsoleMode.place(x=wPercent * 81 - 3 * wDistance, y=height - (hPercent * 0.05 + theHeight) - hDistance,
                             width=wPercent * 10, height=theHeight)
    button_editConfig.place(x=wPercent * 68 + wDistance, y=height - (hPercent * 0.05 + theHeight) - hDistance,
                            width=wPercent * 12, height=theHeight)


def refeshInterfaceArg(Variable):
    positionItems()


def downloadFile(url, file):
    import urllib.request
    try:
        urllib.request.urlretrieve(url, file)
        return True
    except:
        return False


def setConsoleMode():
    global KaSi
    global interface
    global theMode
    theMode = 2
    interface.destroy()
    # Kasi.consoleLoop()


def createList():
    # global isGroup
    global theList
    theList = OrderedDict()
    # isGroup={}
    theList[" "] = False
    theList["[All]"] = 100
    for i in range(0, Kasi.getClientAmount()):
        # isGroup[Kasi.getClientName(i)]=False
        theList[Kasi.getClientName(i)] = i
    for i in range(0, Kasi.getGroupAmount()):
        # isGroup[Kasi.getGroupName(i)]=True
        theList[Kasi.getGroupName(i)] = i
    return theList.keys()


def editConfig():
    global theList
    Kasi.waitOrder(True, "rc")
    theList.clear()
    createList()
    selectMenu = ttk.OptionMenu(
        interface, selectedName, *theList, command=optionsChanged)
    positionItems()
    """"""


def declareButtons():
    global interface
    global inputt
    global button_Send
    global button_ConsoleMode
    global button_editConfig
    global button_Quit
    global selectMenu
    global theList
    Objects = createList()
    interface = Tk()
    inputt = ttk.Entry()
    selectedName = StringVar(interface)
    selectMenu = ttk.OptionMenu(
        interface, selectedName, *theList, command=optionsChanged)
    selectedName.set("ALL")
    button_Quit = ttk.Button(interface, text="Quit", command=interface.destroy)
    button_Send = ttk.Button(interface, text="Send", command=sendOrder)
    button_ConsoleMode = ttk.Button(
        interface, text="Console", command=setConsoleMode)
    button_editConfig = ttk.Button(
        interface, text="editConfig", command=editConfig)

if __name__ == "__main__":
    if platform.system() == "Windows":
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            "KiliTec.Projekt_KaSi.1,0")
        ctypes.windll.kernel32.SetConsoleTitleA(b"Projekt KaSi")
    global theMode
    global Kasi
    global interface
    global theLog
    Kasi = ProjektKaSi()
    theLog = Kasi.getLog()
    theMode = 1
    while True:
        if theMode == 1:
            declareButtons()
            interface.minsize(650, 480)
            theMode = 0
            interface.title("Projekt KaSi")
            if platform.system() == "Windows":
                try:
                    interface.wm_iconbitmap(r'lib\\icon\\icon.ico')
                except:
                    Kasi.createFolder("lib\\icon\\")
                    print("Icon missing trying to downlaod it")
                    if downloadFile("https://drive.google.com/uc?export=download&id=0B6y6X38yrgKkcGplc2xsUDNacTg",
                                    "lib\\icon\\icon.ico"):
                        interface.wm_iconbitmap(r'lib\\icon\\icon.ico')
            else:
                try:
                    interface.wm_iconbitmap(bitmap="@lib/icon/icon.xbm")
                except:
                    Kasi.createFolder("lib/icon/")
                    print("Icon missing trying to downlaod it")
                    if downloadFile("https://drive.google.com/uc?export=download&id=0B6y6X38yrgKkWmt6WHRvMGNoSEU",
                                    "lib/icon/icon.xbm"):
                        interface.wm_iconbitmap(bitmap="@lib/icon/icon.xbm")
            positionItems()
            interface.bind('<F5>', refeshInterfaceArg)
            inputt.bind('<Return>', sendOrderArg)
            interface.bind('<Configure>', refeshInterfaceArg)
            interface.mainloop()
        elif theMode == 2:
            Zustand = True
            while Zustand:
                Zustand = Kasi.waitOrder(FALSE, "")
            theMode = 1
        else:
            theLog.printMessage("Programm closed by User")
            sys.exit(0)
