# -*- coding: utf-8 -*-

'''

Created on 2019-12-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class AppointCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.actionEndTime = None
        self.actionId = None
        self.actionName = None
        self.actionStartTime = None
        self.actionType = None
        self.adapteTerminal = None
        self.enrollInfoCode = None
        self.excludeCitys = None
        self.goodsList = None
        self.goodsSubList = None
        self.noticePhone = None
        self.operateType = None
        self.operateUser = None
        self.otherTerminalSale = None
        self.partType = None
        self.phoneShareContent = None
        self.phoneShareImgUrl = None
        self.phoneShareTitle = None
        self.phoneShareUrl = None
        self.purchaseEndTime = None
        self.purchaseStartTime = None
        self.receiveSys = None
        self.scheduleEndTime = None
        self.scheduleStartTime = None
        self.sendScalperMsg = None
        self.sendUserMsg = None
        self.supervipPurchaseStartTime = None
        self.ticketResaleStartTime = None
        self.transitDate = None
        self.transitFlag = None
        self.vendorCode = None
        self.vendorName = None
        self.vendorType = None
        self.versionNumber = None
        
        self.setParamRule({
        	'actionEndTime':{'allow_empty':False},
        	'actionName':{'allow_empty':False},
        	'actionStartTime':{'allow_empty':False},
        	'actionType':{'allow_empty':False},
        	'adapteTerminal':{'allow_empty':False},
        	'enrollInfoCode':{'allow_empty':False},
        	'excludeCitys':{'allow_empty':False},
        	'noticePhone':{'allow_empty':False},
        	'operateType':{'allow_empty':False},
        	'operateUser':{'allow_empty':False},
        	'otherTerminalSale':{'allow_empty':False},
        	'partType':{'allow_empty':False},
        	'phoneShareContent':{'allow_empty':False},
        	'phoneShareImgUrl':{'allow_empty':False},
        	'phoneShareTitle':{'allow_empty':False},
        	'phoneShareUrl':{'allow_empty':False},
        	'purchaseEndTime':{'allow_empty':False},
        	'purchaseStartTime':{'allow_empty':False},
        	'receiveSys':{'allow_empty':False},
        	'scheduleEndTime':{'allow_empty':False},
        	'scheduleStartTime':{'allow_empty':False},
        	'sendScalperMsg':{'allow_empty':False},
        	'sendUserMsg':{'allow_empty':False},
        	'ticketResaleStartTime':{'allow_empty':False},
        	'transitFlag':{'allow_empty':False},
        	'vendorCode':{'allow_empty':False},
        	'vendorName':{'allow_empty':False},
        	'vendorType':{'allow_empty':False},
        	'versionNumber':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createAppoint'

    def getApiMethod(self):

        return 'suning.custom.appoint.create'



