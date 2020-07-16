# -*- coding: utf-8 -*-

'''

Created on 2017-7-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class ConfirmsubtractModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqXml = None
        
        self.setParamRule({
        	'reqXml':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyConfirmsubtract'

    def getApiMethod(self):

        return 'suning.cmall.confirmsubtract.modify'



