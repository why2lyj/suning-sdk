# -*- coding: utf-8 -*-

'''

Created on 2020-1-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class GetbillQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.info = None
        self.pageNum = None
        self.pgSize = None
        self.type = None
        
        self.setParamRule({
        	'info':{'allow_empty':False},
        	'type':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryGetbill'

    def getApiMethod(self):

        return 'suning.govbus.getbill.query'



