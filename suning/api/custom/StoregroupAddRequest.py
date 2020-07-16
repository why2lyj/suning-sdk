# -*- coding: utf-8 -*-

'''

Created on 2020-5-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class StoregroupAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.snUnionId = None
        
        self.setParamRule({
        	'snUnionId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addStoregroup'

    def getApiMethod(self):

        return 'suning.custom.storegroup.add'



