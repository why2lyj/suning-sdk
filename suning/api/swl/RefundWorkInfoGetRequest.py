# -*- coding: utf-8 -*-

'''

Created on 2016-10-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class RefundWorkInfoGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appointOrderId = None
        
        self.setParamRule({
        	'appointOrderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getRefundWorkInfo'

    def getApiMethod(self):

        return 'suning.swl.refundworkinfo.get'



