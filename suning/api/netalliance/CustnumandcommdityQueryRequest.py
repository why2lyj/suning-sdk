# -*- coding: utf-8 -*-

'''

Created on 2019-5-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class CustnumandcommdityQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'pageNo':{'allow_empty':False},
        	'pageSize':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCustnumandcommdity'

    def getApiMethod(self):

        return 'suning.netalliance.custnumandcommdity.query'



