from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from lib.clients import client
from lib.groups import group
from lib.log import log
import platform

def writetoConfig():
	if platform == "Windows":
		config=open("config\\clients.config","w")
	else:
		config=open("config/clients.config","w")
	for group in theGroup:
		config.write("["+group.getGroupName()+"]\n")
		for i in range(0,group.getClientAmount()):
			config.write(" "+group.getClientName(i)+": "+group.getAddress(i)+"\n")
	config.close()

def unlockClient():
	ButtonClientOK.config(state=NORMAL)
	""""""
	
def lockClient():
	ButtonClientOK.config(state=DISABLED)
	""""""
	
def GroupOK():
	global GroupSelect
	try:
		if groupDict[selectedOption]!=-1:
			if selectedOption!=GroupNameInput.get():
				theGroup[groupDict[selectedOption]].setGroupName(GroupNameInput.get())
		else:
			newName=GroupNameInput.get()
			if newName!="NEW" or newName!="" or newName !=" ":
				createGroup(groupName=newName)
			else:
				messagebox.showerror(title="Empty Name", message="The Group has no name")
	except KeyError:
		newName=GroupNameInput.get()
		if newName!="" or newName !=" ":
			createGroup(groupName=newName)
		else:
			messagebox.showerror(title="Empty Name", message="The Group has no name")
	groupDict.clear()
	GroupNameInput.delete(0,END)
	createGroupList()
	GroupSelect.grid_remove()
	GroupSelect=None
	GroupSelect = ttk.OptionMenu(mainWindow, StringVar(mainWindow), "NEW", *groupDict, command=groupOptionChanged)
	packWindow()

def groupOptionChanged(select):
	global selectedOption
	global ClientSelect
	if select!="None" or select !="NEW":
		GroupNameInput.delete(0,END)
		GroupNameInput.insert(0,str(select))
		
	else:
		ClientNameInput.delete(0,END)
		ClientIPEntry.delete(0,END)
		lockClient()
	selectedOption=select
	ClientSelect.grid_remove()
	ClientSelect=None
	unlockClient()
	clientDict.clear()
	createClientList()
	createClientList()
	ClientSelect=ttk.OptionMenu(mainWindow,StringVar(mainWindow),None,*clientDict,command=clientOptionChanged)
	packWindow()

def clientOptionChanged(select):
	global selectedClientOption
	global ClientSelected
	ClientIPEntry.delete(0,END)
	ClientNameInput.delete(0,END)
	if select!="NEW" or select !="NEW":
		ClientNameInput.insert(0,str(select))
		ClientIPEntry.insert(0,str(theGroup[groupDict[selectedOption]].getClientIP(clientDict[select])))
	else:
		ClientNameInput.insert(0,str(select))
		ClientIPEntry.insert(0,"NONE")
	selectedClientOption=select
def clientOK():
	global ClientSelect
	if selectedOption != None and selectedOption != "NEW" and selectedOption != "None":
		if ClientIPEntry.get()!="" and ClientNameInput!="":
			try:
				if clientDict[selectedClientOption]!=-1:
					theGroup[groupDict[selectedOption]].setClientIP(clientDict[selectedClientOption],ClientIPEntry.get())
					theGroup[groupDict[selectedOption]].changeClientName(clientDict[selectedClientOption],ClientNameInput.get())
				else:
					theGroup[groupDict[selectedOption]].addClient(client(name=ClientNameInput.get(),group=groupDict[selectedOption],Address=ClientIPEntry.get(),log=log(name="none",isOn=FALSE)))
			except KeyError:
				pass
		else:
			messagebox.showerror(title="empty Input",message="Inputs are empty")
		clientDict.clear()
		ClientNameInput.delete(0,END)
		ClientIPEntry.delete(0,END)
		ClientSelect.grid_remove()
		ClientSelect=None
		clientDict.clear()
		createClientList()
		createClientList()
		ClientSelect=ttk.OptionMenu(mainWindow,StringVar(mainWindow),None,*clientDict,command=clientOptionChanged)
		packWindow()
	else:
		messagebox.showerror(title= "no Group selected", message= "No Group Selected")
		ClientNameInput.delete(0,END)
		ClientIPEntry.delete(0,END)		
		
def packWindow():
	labelGroupName.grid(row=0,column=1)
	GroupNameInput.grid(row=0,column=2)
	ButtonGroupOK.grid(row=0,column=3)
	GroupSelect.grid(row=0,column=0)
	ButtonSave.grid(row=2,column=6)
	ClientSelect.grid(row=1,column=0)
	labelClientName.grid(row=1,column=1)
	ClientNameInput.grid(row=1,column=2)
	labelClientIP.grid(row=1,column=3)
	ClientIPEntry.grid(row=1,column=4)
	ButtonClientOK.grid(row=1,column=5)
	
def createGroup(groupName):
	theGroup.append(group(groupName, len(theGroup) + 1))

def addGroupClient(groupID, clientName, clientAddress):
	return theGroup[groupID].addClient(client(name=clientName,group=groupID,Address=clientAddress,log=log(name="none",isOn=FALSE)))
def createFolder(directiory):
	from os import makedirs, path
	if not path.isdir(directiory):
		makedirs(directiory)

def readConfig():
	if platform.system() == "Windows":
		try:
			theconfigFile = open('config\\clients.config', 'r')
		except:
			window = Tk()
			window.withdraw()
			createFolder("config\\")
			File = open('config\\clients.config', 'a')
			File.close()
			messagebox.showinfo("Missing config", "No config Found. Createt an empty one")
			window.destroy()
			return
	else:
		try:
			theconfigFile = open('config/clients.config', 'r')
		except:
			window = Tk()
			window.withdraw()
			createFolder("config/")
			File = open('config/clients.config', 'a')
			File.close()
			messagebox._show("Missing config", "No config Found. Created an empty one")
			window.destroy()
			return
	theConfig = theconfigFile.read().splitlines()
	theconfigFile.close()
	for line in theConfig:
		if line[0] != " ":
			phase=0
			name=""
			for char in line:
				if char=='[' and phase==0:
					phase=1
				elif char != ']':
					name=name+char
			createGroup(name)
			gID = len(theGroup)-1
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
			addGroupClient(groupID=gID,clientName=theName,clientAddress=theAdress)

def createGroupList():
	groupDict.clear()    
	groupDict["NEW"]=-1
	for i in range(0,len(theGroup)):
		groupDict[str(theGroup[i].getGroupName())]=i
	selectedName = "NEW"
	#groupOptionChanged("NEW")
def downloadFile(url, file):
	import urllib.request
	try:
		urllib.request.urlretrieve(url, file)
		return True
	except:
		return False
def createClientList():
	clientDict.clear()
	
	if selectedOption == "NEW" or selectedOption=="None":
		return
	else:
		clientDict["NEW"]=-1
		gID=groupDict[selectedOption]
		for i in range(0,theGroup[gID].getClientAmount()):
			clientDict[theGroup[gID].getClientName(i)]=i
def setIcon():
	if platform.system() == "Windows":
		try:
			import ctypes
			ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("KiliTec.Projekt_KaSiConfigEditor.0,1")
			ctypes.windll.kernel32.SetConsoleTitleA(b"Config Editor")			
			mainWindow.wm_iconbitmap(r'lib\\icon\\icon.ico')
		except:
			Kasi.createFolder("lib\\icon\\")
			print("Icon missing trying to downlaod it")
			if downloadFile("https://drive.google.com/uc?export=download&id=0B6y6X38yrgKkcGplc2xsUDNacTg",
				        "lib\\icon\\icon.ico"):
				mainWindow.wm_iconbitmap(r'lib\\icon\\icon.ico')
	else:
		try:
			mainWindow.wm_iconbitmap(bitmap="@lib/icon/icon.xbm")
		except:
			Kasi.createFolder("lib/icon/")
			print("Icon missing trying to downlaod it")
			if downloadFile("https://drive.google.com/uc?export=download&id=0B6y6X38yrgKkWmt6WHRvMGNoSEU",
		                "lib/icon/icon.xbm"):
				mainWindow.wm_iconbitmap(bitmap="@lib/icon/icon.xbm")
				
	
if __name__=="__main__" or __name__ == "editConfig":
	global theGroup
	global theClient
	global clientDict
	global labelGroupName
	global GroupNameInput
	global ButtonGroupOK
	global GroupSelect
	global selectedName
	global ButtonSave
	global selectedOption
	global ButtonClientOK
	global ClientNameInput
	global labelClientName
	global labelClientIP
	global ClientIPEntry
	global ClientSelect
	selectedOption="None"
	ClientSelect = None
	theGroup=list()
	readConfig()
	groupDict=dict()
	theClient=list()
	clientDict=dict()
	mainWindow=Tk()
	mainWindow.focus_set()
	mainWindow.title(string="Config Editor")
	setIcon()
	labelGroupName=ttk.Label(master=mainWindow,text="Name: ")
	GroupNameInput=ttk.Entry(master=mainWindow)
	ButtonGroupOK=ttk.Button(master=mainWindow,text="OK",command=GroupOK)
	ButtonSave=ttk.Button(master=mainWindow, text="Save",command=writetoConfig)
	createGroupList()
	GroupSelect=ttk.OptionMenu(mainWindow, StringVar(mainWindow),None, *groupDict,command=groupOptionChanged)
	createClientList()
	ClientSelect=ttk.OptionMenu(mainWindow,StringVar(mainWindow),None,*clientDict,command=clientOptionChanged)
	ButtonClientOK=ttk.Button(master=mainWindow,text="OK",command=clientOK)
	ClientNameInput=ttk.Entry(master=mainWindow)
	labelClientName=ttk.Label(master=mainWindow,text="Name: ")
	labelClientIP=ttk.Label(master=mainWindow,text="Address: ")
	ClientIPEntry=ttk.Entry(master=mainWindow)	
	packWindow()
	mainloop()