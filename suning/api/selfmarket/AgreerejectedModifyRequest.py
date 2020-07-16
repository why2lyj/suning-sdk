# -*- coding: utf-8 -*-

'''

Created on 2019-9-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class AgreerejectedModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.agreeMemo = None
        self.backinDate = None
        self.getBackPerson = None
        self.getBackPersonTel = None
        self.omsOrderItemNo = None
        self.returnBackType = None
        self.supplierCode = None
        self.wareHouseCode = None
        
        self.setParamRule({
        	'omsOrderItemNo':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyAgreerejected'

    def getApiMethod(self):

        return 'suning.selfmarket.agreerejected.modify'



