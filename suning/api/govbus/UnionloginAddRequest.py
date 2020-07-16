# -*- coding: utf-8 -*-

'''

Created on 2019-11-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class UnionloginAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.catalog = None
        self.channel = None
        self.comabb = None
        self.comName = None
        self.extra = None
        self.limit = None
        self.limitEndDate = None
        self.limitStartDate = None
        self.limitType = None
        self.role = None
        self.spUid = None
        self.sysCode = None
        self.targetUrl = None
        self.uid = None
        
        self.setParamRule({
        	'comabb':{'allow_empty':False},
        	'comName':{'allow_empty':False},
        	'sysCode':{'allow_empty':False},
        	'uid':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addUnionlogin'

    def getApiMethod(self):

        return 'suning.govbus.unionlogin.add'



