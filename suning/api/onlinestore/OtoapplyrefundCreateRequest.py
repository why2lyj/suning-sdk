# -*- coding: utf-8 -*-

'''

Created on 2020-4-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class OtoapplyrefundCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.applyType = None
        self.operateTime = None
        self.orderId = None
        self.orderItemIdList = None
        self.orderPort = None
        self.pictureURL = None
        self.reasonDes = None
        self.reasonName = None
        self.retReasonCode = None
        
        self.setParamRule({
        	'applyType':{'allow_empty':False},
        	'operateTime':{'allow_empty':False},
        	'orderId':{'allow_empty':False},
        	'reasonName':{'allow_empty':False},
        	'retReasonCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createOtoapplyrefund'

    def getApiMethod(self):

        return 'suning.onlinestore.applyrefund.create'



