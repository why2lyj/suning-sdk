# -*- coding: utf-8 -*-

'''

Created on 2016-4-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class PrivilegeApplyAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.applyHead = None
        self.areaDetail = None
        self.itemDetail = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'applyPrivilegeApplication'

    def getApiMethod(self):

        return 'suning.application.privilege.apply'



