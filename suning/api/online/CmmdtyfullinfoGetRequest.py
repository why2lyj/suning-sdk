# -*- coding: utf-8 -*-

'''

Created on 2019-6-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtyfullinfoGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cmmdtyCode = None
        
        self.setParamRule({
        	'cmmdtyCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getCmmdtyfullinfo'

    def getApiMethod(self):

        return 'suning.online.cmmdtyfullinfo.get'



