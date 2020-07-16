# coding=UTF-8
'''
Created on 2016年2月22日

@author: 15051125
'''     
class Message():
    def __init__(self):
        self.messageId=None
        self.source=None
        self.topic=None
        self.user=None
        self.appKey=None
        self.appId=None
        self.createTime=None
        self.msg=None
        self.sendTime=None
        self.recevieTime=None
        self.messageType=None
    
    def setMessageId(self,parm):
        self.messageId = parm
    def setSource(self,parm):
        self.source = parm
    def setTopic(self,parm):
        self.topic = parm
    def setUser(self,parm):
        self.user = parm
    def setAppKey(self,parm):
        self.appKey = parm
    def setAppId(self,parm):
        self.appId = parm
    def setCreateTime(self,parm):
        self.createTime = parm       
    def setMsg(self,parm):
        self.msg = parm       
    def setSendTime(self,parm):
        self.sendTime = parm        
    def setRecevieTime(self,parm):
        self.recevieTime = parm        
    def setMessageType(self,parm):
        self.messageType = parm 

    def getMessageId(self):
        return self.messageId
    def getSource(self):
        return self.source
    def getTopic(self):
        return self.topic
    def getUser(self):
        return self.user
    def getAppKey(self):
        return self.appKey
    def getAppId(self):
        return self.appId
    def getCreateTime(self):
        return self.createTime       
    def getMsg(self):
        return self.msg     
    def getSendTime(self):
        return self.sendTime       
    def getRecevieTime(self):
        return self.recevieTime      
    def getMessageType(self):
        return self.messageType
        