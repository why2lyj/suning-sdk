# -*- coding: utf-8 -*-

'''

Created on 2020-2-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class BtborderpayinfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.appType = None
        self.channelType = None
        self.device = None
        self.logonUserName = None
        self.notifyUrl = None
        self.orderNos = None
        self.storeCode = None
        self.version = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'channelType':{'allow_empty':False},
        	'device':{'allow_empty':False},
        	'logonUserName':{'allow_empty':False},
        	'notifyUrl':{'allow_empty':False},
        	'storeCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryBtborderpayinfo'

    def getApiMethod(self):

        return 'suning.retailer.btborderpayonlineinfo.query'



