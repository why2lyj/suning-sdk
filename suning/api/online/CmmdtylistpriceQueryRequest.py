# -*- coding: utf-8 -*-

'''

Created on 2019-11-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtylistpriceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.chanId = None
        self.city = None
        self.cmmdtyInfo = None
        self.province = None
        
        self.setParamRule({
        	'chanId':{'allow_empty':False},
        	'province':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCmmdtylistprice'

    def getApiMethod(self):

        return 'suning.online.cmmdtylistprice.query'



