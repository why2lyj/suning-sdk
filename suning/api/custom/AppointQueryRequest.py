# -*- coding: utf-8 -*-

'''

Created on 2019-12-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class AppointQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.actionId = None
        self.partNumber = None
        self.vendorId = None
        
        self.setParamRule({
        	'actionId':{'allow_empty':False},
        	'partNumber':{'allow_empty':False},
        	'vendorId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryAppoint'

    def getApiMethod(self):

        return 'suning.custom.appoint.query'



