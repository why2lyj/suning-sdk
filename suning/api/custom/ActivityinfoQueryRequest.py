# -*- coding: utf-8 -*-

'''

Created on 2019-12-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class ActivityinfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityCode = None
        self.viewNo = None
        self.viewSize = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryActivityinfo'

    def getApiMethod(self):

        return 'suning.custom.activityinfo.query'



