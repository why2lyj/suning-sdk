# -*- coding: utf-8 -*-

'''

Created on 2019-12-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class BookinginfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.actionId = None
        self.snUnionId = None
        
        self.setParamRule({
        	'actionId':{'allow_empty':False},
        	'snUnionId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryBookinginfo'

    def getApiMethod(self):

        return 'suning.custom.bookinginfo.query'



