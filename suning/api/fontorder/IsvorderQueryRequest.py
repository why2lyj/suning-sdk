# -*- coding: utf-8 -*-

'''

Created on 2017-12-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class IsvorderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.buyerCode = None
        self.itemCode = None
        self.orderEndTime = None
        self.orderStartTime = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'orderEndTime':{'allow_empty':False},
        	'orderStartTime':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryIsvorder'

    def getApiMethod(self):

        return 'suning.fontorder.isvorder.query'



