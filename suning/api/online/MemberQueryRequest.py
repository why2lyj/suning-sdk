# -*- coding: utf-8 -*-

'''

Created on 2019-7-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class MemberQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.memberNo = None
        
        self.setParamRule({
        	'memberNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryMember'

    def getApiMethod(self):

        return 'suning.online.member.query'



