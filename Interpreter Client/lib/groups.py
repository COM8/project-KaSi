class group(object):

    __theClients=[]

    def __init__(self, name, groupID ):
        self.__theName=name
        self.__theGroup=groupID
        self.__theClients=[]
    def getGroupName(self):
        return self.__theName
    def getClientName(self,theClientID):
        return self.__theClients[theClientID].getName()
    def getGroup(self):
        return self.__theGroup
    def getClientIP(self,theClientID):
        return self.__theClients[theClientID].getAddress()
    def setClientIP(self,theClientID,newAddress):
        self.__theClients[theClientID].setAddress(newAddress)
    def changeClientName(self,theClientID,newClientName):
        self.__theClients[theClientID].setName(newClientName)
    def getClientAmount(self):
        return len(self.__theClients)
    def getAddress(self,theClientID):
        return self.__theClients[theClientID].getAddress()
    def setGroupName(self,newName):
        self.__theName=newName
    def testClients(self):
        for theClient in self.__theClients:
            if theClient.tryConnection():
                Message=theClient.getName()+ "@" + theClient.getAddress()+": Success"
            else:
                Message=theClient.getName()+ "@" + theClient.getAddress()+": ERROR"
            print(Message)
    def doJOB(self,theOrder):
        for theClient in self.__theClients:
            theAnswer=theClient.sendOrder(theOrder)
            if isinstance(theAnswer, bool):
                if theAnswer:
                    Message=theClient.getName()+ "@" + theClient.getAddress()+": Success"
                else:
                    Message=theClient.getName()+ "@" + theClient.getAddress()+": ERROR"
            else:
                Message=theClient.getName()+ "@" + theClient.getAddress()+" Responce: "+theAnswer
            print(Message)
    def addClient(self,theClient):
        self.__theClients.append(theClient)