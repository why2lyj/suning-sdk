# -*- coding: utf-8 -*-

'''

Created on 2016-1-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class BsSeaOrderDeclareAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.packageOrderId = None
        
        self.setParamRule({
        	'packageOrderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addBsSeaOrderDeclare'

    def getApiMethod(self):

        return 'suning.custom.bsseaorderdeclare.add'



