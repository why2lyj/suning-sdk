# -*- coding: utf-8 -*-

'''

Created on 2018-8-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class WritecarddataGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.opId = None
        self.orgId = None
        self.phoneNumber = None
        self.iccidKey = None
        
        self.setParamRule({
        	'phoneNumber':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getWritecarddata'

    def getApiMethod(self):

        return 'suning.operasale.writecarddata.get'



