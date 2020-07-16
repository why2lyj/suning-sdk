# -*- coding: utf-8 -*-

'''

Created on 2019-10-18

@author: suning

'''

from suning.api.abstract import AbstractApi



class MvstockReceiveRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.deliNumber = None
        self.deliType = None
        self.soCreatDate = None
        self.soCreatTime = None
        self.cmmdtyMvStockInfoList = None
        
        self.setParamRule({
        	'deliNumber':{'allow_empty':False},
        	'deliType':{'allow_empty':False},
        	'soCreatDate':{'allow_empty':False},
        	'soCreatTime':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'receiveMvstock'

    def getApiMethod(self):

        return 'suning.customjlf.mvstock.receive'



