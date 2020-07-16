# -*- coding: utf-8 -*-

'''

Created on 2020-5-18

@author: suning

'''

from suning.api.abstract import AbstractApi



class PullnewinfobytkQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryPullnewinfobytk'

    def getApiMethod(self):

        return 'suning.netalliance.pullnewinfobytk.query'



