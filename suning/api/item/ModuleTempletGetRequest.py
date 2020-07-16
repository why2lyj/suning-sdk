# -*- coding: utf-8 -*-

'''

Created on 2016-5-11

@author: suning

'''

from suning.api.abstract import AbstractApi



class ModuleTempletGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.categoryCode = None
        
        self.setParamRule({
        	'categoryCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getModuleTemplet'

    def getApiMethod(self):

        return 'suning.custom.moduletemplet.get'



