# -*- coding: utf-8 -*-

'''

Created on 2020-3-2

@author: suning

'''

from suning.api.abstract import AbstractApi



class OtoactivityConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityQryCommReqBo = None
        self.businessType = None
        self.customerNo = None
        
        self.setParamRule({
        	'businessType':{'allow_empty':False},
        	'customerNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'confirmOtoactivity'

    def getApiMethod(self):

        return 'suning.onlinestore.activity.confirm'



