# -*- coding: utf-8 -*-

'''

Created on 2020-5-11

@author: suning

'''

from suning.api.abstract import AbstractApi



class SlssAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.bizCode = None
        self.longUrl = None
        
        self.setParamRule({
        	'bizCode':{'allow_empty':False},
        	'longUrl':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addSlss'

    def getApiMethod(self):

        return 'suning.custom.slss.add'



