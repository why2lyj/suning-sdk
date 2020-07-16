# -*- coding: utf-8 -*-

'''

Created on 2017-5-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class FivedaysproduceAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.fivedaysProduce = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'addFivedaysproduce'

    def getApiMethod(self):

        return 'suning.selfmarket.fivedaysproduce.add'



