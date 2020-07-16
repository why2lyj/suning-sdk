# -*- coding: utf-8 -*-

'''

Created on 2019-1-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtybaseinfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.commoditys = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryCmmdtybaseinfo'

    def getApiMethod(self):

        return 'suning.online.cmmdtybaseinfo.query'



