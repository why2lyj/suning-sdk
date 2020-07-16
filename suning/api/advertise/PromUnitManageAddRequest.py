# -*- coding: utf-8 -*-

'''

Created on 2016-10-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class PromUnitManageAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.promotionUnitId = None
        self.promotionUnitType = None
        self.operationType = None
        
        self.setParamRule({
        	'promotionUnitId':{'allow_empty':False},
        	'promotionUnitType':{'allow_empty':False},
        	'operationType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addPromUnitManage'

    def getApiMethod(self):

        return 'suning.advertise.promunitmanage.add'



