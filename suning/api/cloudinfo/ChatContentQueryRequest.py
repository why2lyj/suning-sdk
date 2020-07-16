# -*- coding: utf-8 -*-

'''

Created on 2016-11-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class ChatContentQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.chatId = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'chatId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryChatContent'

    def getApiMethod(self):

        return 'suning.cloudinfo.chatcontent.query'



