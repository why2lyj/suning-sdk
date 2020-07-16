# -*- coding: utf-8 -*-

'''

Created on 2020-6-10

@author: suning

'''

from suning.api.abstract import AbstractApi



class PicdetechAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.dataId = None
        self.picUrl = None
        self.serviceCode = None
        
        self.setParamRule({
        	'dataId':{'allow_empty':False},
        	'picUrl':{'allow_empty':False},
        	'serviceCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addPicdetech'

    def getApiMethod(self):

        return 'suning.custom.picdetech.add'



