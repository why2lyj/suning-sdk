# -*- coding: utf-8 -*-

'''

Created on 2018-3-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class PaidlevelGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.custNum = None
        
        self.setParamRule({
        	'custNum':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getPaidlevel'

    def getApiMethod(self):

        return 'suning.pptv.paidlevel.get'



