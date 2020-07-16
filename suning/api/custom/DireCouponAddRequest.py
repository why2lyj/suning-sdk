# -*- coding: utf-8 -*-

'''

Created on 2018-12-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class DireCouponAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityName = None
        self.baseAmount = None
        self.channelInfo = None
        self.custnumList = None
        self.endTime = None
        self.isAssign = None
        self.productList = None
        self.rewardAmount = None
        self.startTime = None
        
        self.setParamRule({
        	'activityName':{'allow_empty':False},
        	'baseAmount':{'allow_empty':False},
        	'channelInfo':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	'isAssign':{'allow_empty':False},
        	'rewardAmount':{'allow_empty':False},
        	'startTime':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addDireCoupon'

    def getApiMethod(self):

        return 'suning.custom.direcoupon.add'



