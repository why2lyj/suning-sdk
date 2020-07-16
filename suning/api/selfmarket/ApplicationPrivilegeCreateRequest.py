# -*- coding: utf-8 -*-

'''

Created on 2018-7-18

@author: suning

'''

from suning.api.abstract import AbstractApi



class ApplicationPrivilegeCreateRequest(AbstractApi):

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

        return 'createApplicationPrivilege'

    def getApiMethod(self):

        return 'suning.selfmarket.applicationprivilege.create'



