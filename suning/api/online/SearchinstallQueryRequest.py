# -*- coding: utf-8 -*-

'''

Created on 2019-7-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class SearchinstallQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.address = None
        self.chanId = None
        self.city = None
        self.cmmdtyCode = None
        self.county = None
        self.orderItemId = None
        self.province = None
        self.saleNum = None
        self.selectedArrivalTime = None
        self.village = None
        
        self.setParamRule({
        	'address':{'allow_empty':False},
        	'chanId':{'allow_empty':False},
        	'city':{'allow_empty':False},
        	'cmmdtyCode':{'allow_empty':False},
        	'county':{'allow_empty':False},
        	'province':{'allow_empty':False},
        	'saleNum':{'allow_empty':False},
        	'selectedArrivalTime':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'querySearchinstall'

    def getApiMethod(self):

        return 'suning.online.searchinstall.query'



