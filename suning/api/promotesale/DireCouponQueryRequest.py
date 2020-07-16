# -*- coding: utf-8 -*-

'''

Created on 2015-12-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class DireCouponQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityStatus = None
        self.startTime = None
        self.endTime = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryDireCoupon'

    def getApiMethod(self):

        return 'suning.custom.direcoupon.query'



