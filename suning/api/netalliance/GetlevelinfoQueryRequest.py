# -*- coding: utf-8 -*-

'''

Created on 2018-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class GetlevelinfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.memberNo = None
        
        self.setParamRule({
        	'memberNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryGetlevelinfo'

    def getApiMethod(self):

        return 'suning.netalliance.getlevelinfo.query'



