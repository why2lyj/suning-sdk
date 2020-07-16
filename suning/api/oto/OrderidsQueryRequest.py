# -*- coding: utf-8 -*-

'''

Created on 2016-10-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderidsQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.startTime = None
        self.endTime = None
        self.orderType = None
        
        self.setParamRule({
        	'startTime':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryOrderids'

    def getApiMethod(self):

        return 'suning.oto.orderids.query'



