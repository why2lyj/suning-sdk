# -*- coding: utf-8 -*-

'''

Created on 2015-12-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class DireCouponDetailGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        
        self.setParamRule({
        	'activityCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getDireCouponDetail'

    def getApiMethod(self):

        return 'suning.custom.direcoupondetail.get'



