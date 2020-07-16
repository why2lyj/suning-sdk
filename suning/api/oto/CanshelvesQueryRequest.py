# -*- coding: utf-8 -*-

'''

Created on 2016-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class CanshelvesQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.physicalCode = None
        self.categoryCode = None
        self.brandCode = None
        self.productName = None
        self.productCode = None
        self.itemCode = None
        
        self.setParamRule({
        	'physicalCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryCanshelves'

    def getApiMethod(self):

        return 'suning.oto.canshelves.query'



