# -*- coding: utf-8 -*-

'''

Created on 2017-10-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReviewestatusAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reviewestatus = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'addReviewestatus'

    def getApiMethod(self):

        return 'suning.selfmarket.reviewestatus.add'



