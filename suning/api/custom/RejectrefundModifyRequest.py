# -*- coding: utf-8 -*-

'''

Created on 2019-11-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class RejectrefundModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.rejectImage = None
        self.remark = None
        self.returnApplyId = None
        
        self.setParamRule({
        	'remark':{'allow_empty':False},
        	'returnApplyId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyRejectrefund'

    def getApiMethod(self):

        return 'suning.custom.rejectrefund.modify'



