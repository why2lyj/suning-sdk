# -*- coding: utf-8 -*-

'''

Created on 2020-7-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class InteractstoreeffectQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityId = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'activityId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryInteractstoreeffect'

    def getApiMethod(self):

        return 'suning.custom.interactstoreeffect.query'



