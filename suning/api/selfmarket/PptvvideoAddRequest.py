# -*- coding: utf-8 -*-

'''

Created on 2019-10-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class PptvvideoAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.omsList = None
        self.orderCode = None
        self.supplierCode = None
        
        self.setParamRule({
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addPptvvideo'

    def getApiMethod(self):

        return 'suning.selfmarket.pptvvideo.add'



