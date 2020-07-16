# -*- coding: utf-8 -*-

'''

Created on 2015-12-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class AllotFormQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.startTime = None
        self.endTime = None
        self.brandCode = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
       		'startTime':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	'brandCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryAllotForm'

    def getApiMethod(self):

        return 'suning.selfmarket.allotform.query'

