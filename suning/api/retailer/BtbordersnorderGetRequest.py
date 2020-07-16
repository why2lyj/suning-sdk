# -*- coding: utf-8 -*-

'''

Created on 2019-7-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class BtbordersnorderGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appId = None
        self.outOrderNo = None
        
        self.setParamRule({
        	'appId':{'allow_empty':False},
        	'outOrderNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getBtbordersnorder'

    def getApiMethod(self):

        return 'suning.retailer.btbordersnorder.get'



