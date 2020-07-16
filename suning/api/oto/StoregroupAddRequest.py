# -*- coding: utf-8 -*-

'''

Created on 2018-10-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class StoregroupAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.groupName = None
        self.groupRemark = None
        
        self.setParamRule({
        	'groupName':{'allow_empty':False},
        	'groupRemark':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addStoregroup'

    def getApiMethod(self):

        return 'suning.oto.storegroup.add'



