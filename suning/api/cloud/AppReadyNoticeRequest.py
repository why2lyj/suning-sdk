# -*- coding: utf-8 -*-

'''

Created on 2016-3-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class AppReadyNoticeRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.serialId = None
        self.productInsId = None
        self.orderId = None
        self.orderType = None
        self.result = None
        self.message = None
        
        self.setParamRule({
        	'serialId':{'allow_empty':False},
        	'productInsId':{'allow_empty':False},
        	'orderId':{'allow_empty':False},
        	'orderType':{'allow_empty':False},
        	'result':{'allow_empty':False},
        	'message':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'noticeAppComplete'

    def getApiMethod(self):

        return 'suning.cloud.appcomplete.notice'



