# -*- coding: utf-8 -*-

'''

Created on 2019-9-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class RejectexchangeModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.changeApplyId = None
        self.rejectImage = None
        self.remark = None
        
        self.setParamRule({
        	'changeApplyId':{'allow_empty':False},
        	'remark':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyRejectexchange'

    def getApiMethod(self):

        return 'suning.custom.rejectexchange.modify'



