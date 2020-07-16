# -*- coding: utf-8 -*-

'''

Created on 2019-12-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class CansalechangeQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.beginTime = None
        self.endTime = None
        
        self.setParamRule({
        	'beginTime':{'allow_empty':False},
        	'endTime':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCansalechange'

    def getApiMethod(self):

        return 'suning.defctive.cansalechange.query'



