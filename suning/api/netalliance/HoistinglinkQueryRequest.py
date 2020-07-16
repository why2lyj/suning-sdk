# -*- coding: utf-8 -*-

'''

Created on 2020-5-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class HoistinglinkQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.goodsCode = None
        self.mertCode = None
        self.subUser = None
        self.adBookId = None
        self.backurl = None
        
        self.setParamRule({
        	'goodsCode':{'allow_empty':False},
        	'mertCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryHoistinglink'

    def getApiMethod(self):

        return 'suning.netalliance.hoistinglink.query'



