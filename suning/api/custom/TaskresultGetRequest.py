# -*- coding: utf-8 -*-

'''

Created on 2020-4-3

@author: suning

'''

from suning.api.abstract import AbstractApi



class TaskresultGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.taskId = None
        
        self.setParamRule({
        	'taskId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getTaskresult'

    def getApiMethod(self):

        return 'suning.custom.taskresult.get'



