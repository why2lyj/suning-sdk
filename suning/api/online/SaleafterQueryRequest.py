# -*- coding: utf-8 -*-

'''

Created on 2019-9-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class SaleafterQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cmmdtyCode = None
        self.custNo = None
        self.pn = None
        self.prdImgUrl = None
        self.prdPrice = None
        self.prdurl = None
        self.scene = None
        
        self.setParamRule({
        	'custNo':{'allow_empty':False},
        	'scene':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'querySaleafter'

    def getApiMethod(self):

        return 'suning.online.saleafter.query'



