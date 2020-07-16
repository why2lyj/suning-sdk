# -*- coding: utf-8 -*-

'''

Created on 2020-3-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class KuaishounewpromotionurlGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.backUrl = None
        self.channelCode = None
        self.itemKey = None
        self.pid = None
        
        self.setParamRule({
        	'itemKey':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getKuaishounewpromotionurl'

    def getApiMethod(self):

        return 'suning.netalliance.kuaishounewpromotionurl.get'



