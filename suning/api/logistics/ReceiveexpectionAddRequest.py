# -*- coding: utf-8 -*-

'''

Created on 2017-6-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReceiveexpectionAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.exType = None
        self.logisticOrderId = None
        self.remark = None
        self.storeOutCompany = None
        
        self.setParamRule({
        	'exType':{'allow_empty':False},
        	'logisticOrderId':{'allow_empty':False},
        	'remark':{'allow_empty':False},
        	'storeOutCompany':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addReceiveexpection'

    def getApiMethod(self):

        return 'suning.logistics.receiveexpection.add'



