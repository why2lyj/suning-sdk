# -*- coding: utf-8 -*-

'''

Created on 2017-3-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class ExpressorderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.innerOrderId = None
        
        self.setParamRule({
        	'innerOrderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryExpressorder'

    def getApiMethod(self):

        return 'suning.fourps.expressorder.query'



