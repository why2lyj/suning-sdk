# -*- coding: utf-8 -*-

'''

Created on 2014-9-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReplyreviewAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderCode = None
        self.productCode = None
        self.replyContent = None



    def getApiBizName(self):

        return 'addReplyReview'



    def getApiMethod(self):

        return 'suning.custom.replyreview.add'



