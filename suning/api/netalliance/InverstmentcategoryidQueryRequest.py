# -*- coding: utf-8 -*-

'''

Created on 2019-11-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class InverstmentcategoryidQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryInverstmentcategoryid'

    def getApiMethod(self):

        return 'suning.netalliance.inverstmentcategoryid.query'



