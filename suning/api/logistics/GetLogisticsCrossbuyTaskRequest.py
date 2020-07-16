# -*- coding: utf-8 -*-

'''

Created on 2015-1-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class GetLogisticsCrossbuyTaskRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.logisticOrderId = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getLogisticsCrossbuyTask'

    def getApiMethod(self):

        return 'suning.logistics.crossbuytask.get'



