# -*- coding: utf-8 -*-

'''

Created on 2020-3-31

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderinfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endTime = None
        self.orderId = None
        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryOrderinfo'

    def getApiMethod(self):

        return 'suning.netalliance.orderinfo.query'



