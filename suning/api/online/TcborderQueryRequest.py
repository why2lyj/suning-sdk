# -*- coding: utf-8 -*-

'''

Created on 2019-4-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class TcborderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderNo = None
        
        self.setParamRule({
        	'orderNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryTcborderquery'

    def getApiMethod(self):

        return 'suning.online.tcborderquery.query'



