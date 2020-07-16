# -*- coding: utf-8 -*-

'''

Created on 2019-5-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class PicfilesQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        self.searchName = None
        self.classifysCode = None
        self.startDate = None
        self.endDate = None
        self.fileType = None
        self.vendorCode = None
        
        self.setParamRule({
        	'pageNo':{'allow_empty':False},
        	'pageSize':{'allow_empty':False},
        	'fileType':{'allow_empty':False},
        	'vendorCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryPicfiles'

    def getApiMethod(self):

        return 'suning.custom.picfiles.query'



