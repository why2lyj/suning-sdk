# -*- coding: utf-8 -*-

'''

Created on 2015-8-7

@author: suning

'''

from suning.api.abstract import AbstractApi



class OuterOrderModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.oriSys = None
        self.orderItems = None
        
        self.setParamRule({
        	
        	})

    def getApiBizName(self):

        return 'modifyOuterOrder'

    def getApiMethod(self):

        return 'suning.logistics.outerorder.modify'



