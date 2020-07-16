# -*- coding: utf-8 -*-

'''

Created on 2018-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class RejectsOrdQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endTime = None
        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        self.supplierCode = None
        
        self.setParamRule({
        	'endTime':{'allow_empty':False},
        	'startTime':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryRejectsOrd'

    def getApiMethod(self):

        return 'suning.selfmarket.rejectorder.query'



