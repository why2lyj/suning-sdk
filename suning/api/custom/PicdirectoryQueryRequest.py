# -*- coding: utf-8 -*-

'''

Created on 2020-6-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class PicdirectoryQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.parentDirCode = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryPicdirectory'

    def getApiMethod(self):

        return 'suning.custom.picdirectory.query'



