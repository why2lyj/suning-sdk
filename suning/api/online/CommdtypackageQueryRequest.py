# -*- coding: utf-8 -*-

'''

Created on 2019-3-21

@author: suning

'''

from suning.api.abstract import AbstractApi



class CommdtypackageQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.packageID = None
        
        self.setParamRule({
        	'packageID':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCommdtypackage'

    def getApiMethod(self):

        return 'suning.online.commdtypackage.query'



