# -*- coding: utf-8 -*-

'''

Created on 2019-10-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class TwittersuccessQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.beginDate = None
        self.endDate = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'beginDate':{'allow_empty':False},
        	'endDate':{'allow_empty':False},
        	'pageNo':{'allow_empty':False},
        	'pageSize':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryTwittersuccess'

    def getApiMethod(self):

        return 'suning.netalliance.twittersuccess.query'



