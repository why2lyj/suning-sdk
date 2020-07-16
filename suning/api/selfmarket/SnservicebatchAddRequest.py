# -*- coding: utf-8 -*-

'''

Created on 2017-6-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class SnservicebatchAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.sninstallDetail = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'addSnservicebatch'

    def getApiMethod(self):

        return 'suning.selfmarket.snservicebatch.add'



