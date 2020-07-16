# -*- coding: utf-8 -*-

'''

Created on 2020-7-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class ToolsellerAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.channel = None
        self.phone = None
        self.positionId = None
        
        self.setParamRule({
        	'channel':{'allow_empty':False},
        	'phone':{'allow_empty':False},
        	'positionId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addToolseller'

    def getApiMethod(self):

        return 'suning.netalliance.toolseller.add'



