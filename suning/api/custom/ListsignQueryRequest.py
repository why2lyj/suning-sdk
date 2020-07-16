# -*- coding: utf-8 -*-

'''

Created on 2020-4-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class ListsignQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.accessKeyId = None
        self.accessSign = None
        self.name = None
        self.pageNo = None
        self.pageSize = None
        self.timeStamp = None
        
        self.setParamRule({
        	'accessKeyId':{'allow_empty':False},
        	'accessSign':{'allow_empty':False},
        	'pageNo':{'allow_empty':False},
        	'pageSize':{'allow_empty':False},
        	'timeStamp':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryListsign'

    def getApiMethod(self):

        return 'suning.custom.sign.query'



