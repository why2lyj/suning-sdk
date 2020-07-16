# -*- coding: utf-8 -*-

'''

Created on 2020-6-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class MsgtaskCancelRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.taskId = None
        
        self.setParamRule({
        	'taskId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'cancelMsgtask'

    def getApiMethod(self):

        return 'suning.custom.msgtask.cancel'



