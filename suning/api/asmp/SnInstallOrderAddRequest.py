# -*- coding: utf-8 -*-

'''

Created on 2016-5-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class SnInstallOrderAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.recordGuid = None
        self.itemGuid = None
        self.srvOrdId = None
        self.srvOrdType = None
        self.zb2bFlag = None
        self.jsDetail = None
        self.jyDetail = None
        
        self.setParamRule({
        	'recordGuid':{'allow_empty':False},
        	'itemGuid':{'allow_empty':False},
        	'srvOrdId':{'allow_empty':False},
        	'srvOrdType':{'allow_empty':False},
        	'zb2bFlag':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addSnInstallOrder'

    def getApiMethod(self):

        return 'suning.asmp.sninstallorder.add'



