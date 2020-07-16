# -*- coding: utf-8 -*-

'''

Created on 2018-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderAccountQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endDate = None
        self.orderStatus = None
        self.pageNo = None
        self.pageSize = None
        self.startDate = None
        
        self.setParamRule({
        	'endDate':{'allow_empty':False},
        	'orderStatus':{'allow_empty':False},
        	'startDate':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryOrderAccount'

    def getApiMethod(self):

        return 'suning.govbus.orderaccount.query'



