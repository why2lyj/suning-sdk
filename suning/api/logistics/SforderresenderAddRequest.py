# -*- coding: utf-8 -*-

'''

Created on 2017-6-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class SforderresenderAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.mailNo = None
        self.orderNo = None
        
        self.setParamRule({
        	'mailNo':{'allow_empty':False},
        	'orderNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addSforderresender'

    def getApiMethod(self):

        return 'suning.logistics.sforderresender.add'



