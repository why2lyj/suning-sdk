# -*- coding: utf-8 -*-

'''

Created on 2019-1-7

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReservefpsQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.uuid = None
        self.outOrderId = None
        
        self.setParamRule({
        	'uuid':{'allow_empty':False},
        	'outOrderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryReservefps'

    def getApiMethod(self):

        return 'suning.selfmarket.reservefps.query'



