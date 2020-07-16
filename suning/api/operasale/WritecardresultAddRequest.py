# -*- coding: utf-8 -*-

'''

Created on 2018-8-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class WritecardresultAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.opId = None
        self.orgId = None
        self.phoneNumber = None
        self.resultCode = None
        self.resultResc = None
        self.iccid = None
        self.imsi = None
        self.transId = None
        
        self.setParamRule({
        	'phoneNumber':{'allow_empty':False},
        	'resultCode':{'allow_empty':False},
        	'iccid':{'allow_empty':False},
        	'imsi':{'allow_empty':False},
        	'transId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addWritecardresult'

    def getApiMethod(self):

        return 'suning.operasale.writecardresult.add'



