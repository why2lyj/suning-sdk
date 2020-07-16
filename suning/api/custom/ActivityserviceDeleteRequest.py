# -*- coding: utf-8 -*-

'''

Created on 2019-12-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class ActivityserviceDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        self.remarks = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'deleteActivityservice'

    def getApiMethod(self):

        return 'suning.custom.activityservice.delete'



