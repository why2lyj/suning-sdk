# -*- coding: utf-8 -*-

'''

Created on 2019-9-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class ActivityGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityId = None
        self.chanId = None
        self.cmmdtyCode = None
        
        self.setParamRule({
        	'cmmdtyCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getActivity'

    def getApiMethod(self):

        return 'suning.online.activity.get'



