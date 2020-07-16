# -*- coding: utf-8 -*-

'''

Created on 2016-10-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class PromPlanManageAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.promotionId = None
        self.promotionType = None
        self.operationType = None
        
        self.setParamRule({
        	'promotionId':{'allow_empty':False},
        	'promotionType':{'allow_empty':False},
        	'operationType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addPromPlanManage'

    def getApiMethod(self):

        return 'suning.advertise.promplanmanage.add'



