# -*- coding: utf-8 -*-

'''

Created on 2019-7-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class LabelportraitQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.reqJson = None
        
        self.setParamRule({
        	'reqJson':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryLabelportrait'

    def getApiMethod(self):

        return 'suning.market.labelportrait.query'



