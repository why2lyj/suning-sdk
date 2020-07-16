# -*- coding: utf-8 -*-

'''

Created on 2018-12-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class GetperiodlimitQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.userAccount = None
        
        self.setParamRule({
        	'userAccount':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryGetperiodlimit'

    def getApiMethod(self):

        return 'suning.govbus.getperiodlimit.query'



