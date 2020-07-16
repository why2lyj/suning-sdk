# -*- coding: utf-8 -*-

'''

Created on 2020-5-18

@author: suning

'''

from suning.api.abstract import AbstractApi



class NicknameGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.custNum = None
        
        self.setParamRule({
        	'custNum':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getNickname'

    def getApiMethod(self):

        return 'suning.custom.nickname.get'



