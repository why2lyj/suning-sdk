# -*- coding: utf-8 -*-

'''

Created on 2019-8-1

@author: suning

'''

from suning.api.abstract import AbstractApi



class ChannelorderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.channelCode = None
        self.endTime = None
        self.orderLineStatus = None
        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        
        self.setParamRule({
        	'channelCode':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	'orderLineStatus':{'allow_empty':False},
        	'startTime':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryChannelorder'

    def getApiMethod(self):

        return 'suning.netalliance.channelorder.query'



