# -*- coding: utf-8 -*-

'''

Created on 2015-6-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReportGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.qtCode = None
        self.qtOrderCode = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'getReport'

    def getApiMethod(self):

        return 'suning.fws.report.get'



