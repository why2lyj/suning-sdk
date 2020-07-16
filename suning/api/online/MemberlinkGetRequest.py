# -*- coding: utf-8 -*-

'''

Created on 2019-9-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class MemberlinkGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.memberNo = None
        self.mobileNo = None
        self.targetUrl = None
        
        self.setParamRule({
        	'memberNo':{'allow_empty':False},
        	'targetUrl':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getMemberlink'

    def getApiMethod(self):

        return 'suning.online.memberlink.get'



