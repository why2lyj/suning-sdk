# -*- coding: utf-8 -*-

'''

Created on 2018-8-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class XdsalesdetailQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.statisDate = None
        self.storeCode = None
        
        self.setParamRule({
        	'statisDate':{'allow_empty':False},
        	'storeCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryXdsalesdetail'

    def getApiMethod(self):

        return 'suning.retail.xdsalesdetail.query'



