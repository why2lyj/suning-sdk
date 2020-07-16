# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class JsydcmmdtycategoryQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.catClass = None
        self.parentId = None
        self.pnumber = None
        self.psize = None
        self.token = None
        
        self.setParamRule({
        	'pnumber':{'allow_empty':False},
        	'psize':{'allow_empty':False},
        	'token':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryJsydcmmdtycategory'

    def getApiMethod(self):

        return 'suning.retailer.jsydcmmdtycategory.query'



