# -*- coding: utf-8 -*-

'''

Created on 2020-4-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class PointquotaQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appCode = None
        self.custNum = None
        self.sourceChannel = None
        self.sourceSystemNo = None
        self.tranTimestamp = None
        
        self.setParamRule({
        	'appCode':{'allow_empty':False},
        	'custNum':{'allow_empty':False},
        	'sourceChannel':{'allow_empty':False},
        	'sourceSystemNo':{'allow_empty':False},
        	'tranTimestamp':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryPointquota'

    def getApiMethod(self):

        return 'suning.custexpand.pointquota.query'



