# -*- coding: utf-8 -*-

'''

Created on 2019-12-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class QuerypgappletqrcodeurlGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityId = None
        self.page = None
        self.subPromoter = None
        
        self.setParamRule({
        	'activityId':{'allow_empty':False},
        	'page':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getQuerypgappletqrcodeurl'

    def getApiMethod(self):

        return 'suning.netalliance.querypgappletqrcodeurl.get'



