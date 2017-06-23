import platform
from time import gmtime, strftime


class log(object):
    """Client logger"""

    def __init__(self, name,isOn):
        self.doLog=isOn
        if self.doLog:
            if platform.system() == "Windows":
                self.fileName = "log\\" + str(name)
            else:
                self.fileName = "log/" + str(name)
            try:
                test= open(self.fileName,"a")
                test.close()
            except FileNotFoundError or FileExistsError:
                import tkinter as tk
                from tkinter import messagebox
                window=tk.Tk()
                window.withdraw()
                Answer=messagebox.askyesno("No Log Folder","Do you want to create one?")
                if Answer:
                    from os import makedirs,path
                    if not path.isdir("log/"):
                        makedirs("log/")
                    window.destroy()
                else:
                    self.doLog=False
                    window.destroy()



    def writetoFile(self, message):
        newMassage = message + "\n"
        logFile = open(self.fileName, "a")
        logFile.write(newMassage)
        logFile.close()
    @staticmethod
    def getTime():
        return str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

    def printWarning(self, warning):
        print(warning)
        if self.doLog:
            message = self.getTime() + "\t[WARNING]\t" + warning
            self.writetoFile(message)


    def printError(self, fehler):
        print(fehler)
        if self.doLog:
            message = self.getTime() + "\t[ ERROR ]\t" + fehler
            self.writetoFile(message)

    def printMessage(self, Message):
        print(Message)
        if self.doLog:
            message = self.getTime() + "\t[MESSAGE]\t" + Message
            self.writetoFile(message)
