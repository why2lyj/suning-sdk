# -*- coding: utf-8 -*-

'''

Created on 2016-5-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReplyCmReviewAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.commodityReviewId = None
        self.deceiveType = None
        self.type = None
        self.replyContent = None
        
        self.setParamRule({
        	'commodityReviewId':{'allow_empty':False},
        	'deceiveType':{'allow_empty':False},
        	'type':{'allow_empty':False},
        	'replyContent':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addReplyCmReview'

    def getApiMethod(self):

        return 'suning.custom.replycmreview.add'



