# -*- coding: utf-8 -*-

'''

Created on 2015-6-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class CancelRefundWorkInfoRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appointOrderId = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'cancelRefundWorkInfo'

    def getApiMethod(self):

        return 'suning.swl.refundworkinfo.cancel'



