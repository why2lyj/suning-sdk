# -*- coding: utf-8 -*-

'''

Created on 2019-7-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class CitystrategycorpinfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.strategyNo = None
        
        self.setParamRule({
        	'pageNo':{'allow_empty':False},
        	'pageSize':{'allow_empty':False},
        	'strategyNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCitystrategycorpinfo'

    def getApiMethod(self):

        return 'suning.netalliance.citystrategycorpinfo.query'



