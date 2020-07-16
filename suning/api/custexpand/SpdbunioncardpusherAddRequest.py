# -*- coding: utf-8 -*-

'''

Created on 2019-7-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class SpdbunioncardpusherAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.data = None
        self.sign = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'addSpdbunioncardpusher'

    def getApiMethod(self):

        return 'suning.custexpand.spdbunioncardpusher.add'



