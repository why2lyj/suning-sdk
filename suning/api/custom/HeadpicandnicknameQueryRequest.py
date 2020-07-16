# -*- coding: utf-8 -*-

'''

Created on 2019-10-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class HeadpicandnicknameQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.mixCustNum = None
        
        self.setParamRule({
        	'mixCustNum':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryHeadpicandnickname'

    def getApiMethod(self):

        return 'suning.custom.headpicandnickname.query'



