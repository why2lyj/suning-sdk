# -*- coding: utf-8 -*-

'''

Created on 2018-10-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class StoregrouprefAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.groupCode = None
        self.storeCode = None
        
        self.setParamRule({
        	'groupCode':{'allow_empty':False},
        	'storeCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addStoregroupref'

    def getApiMethod(self):

        return 'suning.oto.storegroupref.add'



