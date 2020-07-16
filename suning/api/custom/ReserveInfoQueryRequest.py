# -*- coding: utf-8 -*-

'''

Created on 2020-2-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReserveInfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.actionId = None
        self.snUnionId = None
        self.partnumber = None
        self.beginTime = None
        
        self.setParamRule({
        	'actionId':{'allow_empty':False},
        	'snUnionId':{'allow_empty':False},
        	'partnumber':{'allow_empty':False},
        	'beginTime':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryReserveInfo'

    def getApiMethod(self):

        return 'suning.custom.reserve.query'



