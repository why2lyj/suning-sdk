# -*- coding: utf-8 -*-

'''

Created on 2017-8-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderinfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        self.endTime = None
        
        self.setParamRule({
        	'startTime':{'allow_empty':False},
        	'endTime':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryOrderinfo'

    def getApiMethod(self):

        return 'suning.oto.orderinfo.query'



