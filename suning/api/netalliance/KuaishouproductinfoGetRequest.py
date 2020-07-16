# -*- coding: utf-8 -*-

'''

Created on 2020-5-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class KuaishouproductinfoGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.backUrl = None
        self.channelCode = None
        self.couponMark = None
        self.relItemUrl = None
        
        self.setParamRule({
        	'relItemUrl':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getKuaishouproductinfo'

    def getApiMethod(self):

        return 'suning.netalliance.kuaishouproductinfo.get'



