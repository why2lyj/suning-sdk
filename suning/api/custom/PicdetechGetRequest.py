# -*- coding: utf-8 -*-

'''

Created on 2020-6-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class PicdetechGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.dataId = None
        
        self.setParamRule({
        	'dataId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getPicdetech'

    def getApiMethod(self):

        return 'suning.custom.picdetech.get'



