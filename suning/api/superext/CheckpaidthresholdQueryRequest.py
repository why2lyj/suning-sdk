# -*- coding: utf-8 -*-

'''

Created on 2019-11-18

@author: suning

'''

from suning.api.abstract import AbstractApi



class CheckpaidthresholdQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.appCode = None
        self.businessSource = None
        self.extSystemId = None
        self.mixCustNum = None
        self.mobileNum = None
        self.packageId = None
        
        self.setParamRule({
        	'appCode':{'allow_empty':False},
        	'extSystemId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryCheckpaidthreshold'

    def getApiMethod(self):

        return 'suning.superext.checkpaidthreshold.query'



