# -*- coding: utf-8 -*-

'''

Created on 2018-8-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class CloudsalesreportQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.statisStartDate = None
        self.statisEndDate = None
        self.vendorCd = None
        self.strCd = None
        self.strNm = None
        self.gdsCd = None
        self.vendorGds = None
        
        self.setParamRule({
        	'statisStartDate':{'allow_empty':False},
        	'statisEndDate':{'allow_empty':False},
        	'vendorCd':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryCloudsalesreport'

    def getApiMethod(self):

        return 'suning.selfmarket.cloudsalesreport.query'



