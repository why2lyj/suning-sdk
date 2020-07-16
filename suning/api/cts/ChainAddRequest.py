# -*- coding: utf-8 -*-

'''

Created on 2018-5-30

@author: suning

'''

from suning.api.abstract import AbstractApi



class ChainAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.channelName = None
        self.includeTraceId = None
        self.lastMemberCode = None
        self.lastPoint = None
        self.lastRoleId = None
        self.memberCode = None
        self.memberName = None
        self.msg = None
        self.point = None
        self.roleId = None
        self.traceId = None
        
        self.setParamRule({
        	'channelName':{'allow_empty':False},
        	'memberCode':{'allow_empty':False},
        	'memberName':{'allow_empty':False},
        	'msg':{'allow_empty':False},
        	'point':{'allow_empty':False},
        	'roleId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addChain'

    def getApiMethod(self):

        return 'suning.cts.chain.add'



