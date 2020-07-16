# -*- coding: utf-8 -*-

'''

Created on 2015-8-7

@author: suning

'''

from suning.api.abstract import AbstractApi



class OuterOrderAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.oriSys = None
        self.orderItems = None
        
        self.setParamRule({
        	'oriSys':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addOuterOrder'

    def getApiMethod(self):

        return 'suning.logistics.outerorder.add'



