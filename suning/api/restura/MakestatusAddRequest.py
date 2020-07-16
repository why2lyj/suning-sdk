# -*- coding: utf-8 -*-

'''

Created on 2019-8-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class MakestatusAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.makeStatus = None
        self.orderIds = None
        self.storeCode = None
        
        self.setParamRule({
        	'makeStatus':{'allow_empty':False},
        	'storeCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addMakestatus'

    def getApiMethod(self):

        return 'suning.restura.makestatus.add'



