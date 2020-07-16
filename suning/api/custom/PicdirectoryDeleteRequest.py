# -*- coding: utf-8 -*-

'''

Created on 2020-6-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class PicdirectoryDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.dirCode = None
        
        self.setParamRule({
        	'dirCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'deletePicdirectory'

    def getApiMethod(self):

        return 'suning.custom.picdirectory.delete'



