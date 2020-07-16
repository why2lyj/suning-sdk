# -*- coding: utf-8 -*-

'''

Created on 2018-6-26

@author: suning

'''

from suning.api.abstract import AbstractApi



class AbnormalQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.abnormalCode = None
        self.pageNo = None
        self.pageSize = None
        self.saleStatus = None
        self.senario = None
        self.supplierCode = None
        
        self.setParamRule({
        	'abnormalCode':{'allow_empty':False},
        	'senario':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryAbnormal'

    def getApiMethod(self):

        return 'suning.custom.abnormal.query'



