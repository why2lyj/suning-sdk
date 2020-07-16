# -*- coding: utf-8 -*-

'''

Created on 2018-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class CommodityparamQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cmmdtyCode = None
        
        self.setParamRule({
        	'cmmdtyCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCommodityparam'

    def getApiMethod(self):

        return 'suning.online.commodityparam.query'



