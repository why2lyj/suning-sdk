# -*- coding: utf-8 -*-

'''

Created on 2018-3-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class GetproductcodeQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.applycode = None
        self.suppliercmcode = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryGetproductcode'

    def getApiMethod(self):

        return 'suning.custom.getproductcode.query'



