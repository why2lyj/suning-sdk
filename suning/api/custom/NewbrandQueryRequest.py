# -*- coding: utf-8 -*-

'''

Created on 2017-2-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class NewbrandQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.targetChannel = None
        self.brandCode = None
        self.categoryCode = None
        self.brandName = None
        
        self.setParamRule({
        	'categoryCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryNewbrand'

    def getApiMethod(self):

        return 'suning.custom.newbrand.query'



