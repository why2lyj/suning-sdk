# -*- coding: utf-8 -*-

'''

Created on 2015-12-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class RefundWorkInfoDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'deleteRefundWorkInfo'

    def getApiMethod(self):

        return 'suning.fourps.refundworkinfo.delete'



