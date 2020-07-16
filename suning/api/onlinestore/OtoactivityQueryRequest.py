# -*- coding: utf-8 -*-

'''

Created on 2020-2-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class OtoactivityQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityId = None
        self.businessType = None
        self.commCode = None
        self.customerNo = None
        self.storeCode = None
        
        self.setParamRule({
        	'activityId':{'allow_empty':False},
        	'businessType':{'allow_empty':False},
        	'commCode':{'allow_empty':False},
        	'customerNo':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryOtoactivity'

    def getApiMethod(self):

        return 'suning.onlinestore.activity.query'



