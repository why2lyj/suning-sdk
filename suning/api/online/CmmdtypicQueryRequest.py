# -*- coding: utf-8 -*-

'''

Created on 2020-1-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtypicQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cmmdtyCode = None
        self.picType = None
        
        self.setParamRule({
        	'cmmdtyCode':{'allow_empty':False},
        	'picType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCmmdtypic'

    def getApiMethod(self):

        return 'suning.online.cmmdtypic.query'



