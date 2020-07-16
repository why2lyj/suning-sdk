# -*- coding: utf-8 -*-

'''

Created on 2020-6-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class NPicAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.picContent = None
        self.dirCode = None
        
        self.setParamRule({
        	'picContent':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addNPic'

    def getApiMethod(self):

        return 'suning.custom.npic.add'



