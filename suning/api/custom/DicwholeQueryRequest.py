# -*- coding: utf-8 -*-

'''

Created on 2019-7-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class DicwholeQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.operType = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'operType':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryDicwhole'

    def getApiMethod(self):

        return 'suning.custom.dicwhole.query'



