# -*- coding: utf-8 -*-

'''

Created on 2020-5-18

@author: suning

'''

from suning.api.abstract import AbstractApi



class SuncodeCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageUrl = None
        self.posterHeight = None
        self.posterUrl = None
        self.posterWith = None
        self.sceneParam = None
        self.sunCodeX = None
        self.sunCodeY = None
        self.width = None
        
        self.setParamRule({
        	'pageUrl':{'allow_empty':False},
        	'sceneParam':{'allow_empty':False},
        	'width':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createSuncode'

    def getApiMethod(self):

        return 'suning.custom.suncode.create'



