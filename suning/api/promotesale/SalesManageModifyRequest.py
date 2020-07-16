# -*- coding: utf-8 -*-

'''

Created on 2015-7-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class SalesManageModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        self.operateType = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False},
        	'operateType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifySalesManage'

    def getApiMethod(self):

        return 'suning.custom.salesmanage.modify'



