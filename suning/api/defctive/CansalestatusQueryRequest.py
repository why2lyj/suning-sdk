# -*- coding: utf-8 -*-

'''

Created on 2019-12-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class CansalestatusQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.serialNum = None
        
        self.setParamRule({
        	'serialNum':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCansalestatus'

    def getApiMethod(self):

        return 'suning.defctive.cansalestatus.query'



