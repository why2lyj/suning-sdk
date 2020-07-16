# -*- coding: utf-8 -*-

'''

Created on 2020-6-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class PicdirectoryAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.dirName = None
        self.parentDirCode = None
        
        self.setParamRule({
        	'dirName':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addPicdirectory'

    def getApiMethod(self):

        return 'suning.custom.picdirectory.add'



