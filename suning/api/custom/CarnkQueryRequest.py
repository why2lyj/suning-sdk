# -*- coding: utf-8 -*-

'''

Created on 2019-11-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class CarnkQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.seriesId = None
        
        self.setParamRule({
        	'seriesId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCarnk'

    def getApiMethod(self):

        return 'suning.custom.carnk.query'



