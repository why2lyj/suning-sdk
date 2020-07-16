# -*- coding: utf-8 -*-

'''

Created on 2018-1-5

@author: suning

'''

from suning.api.abstract import AbstractApi



class orderNoteModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.colorMarkFlag = None
        self.noteContent = None
        self.noteFlag = None
        self.orderCode = None
        
        self.setParamRule({
        	'colorMarkFlag':{'allow_empty':False},
        	'noteContent':{'allow_empty':False},
        	'noteFlag':{'allow_empty':False},
        	'orderCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'orderNote'

    def getApiMethod(self):

        return 'suning.custom.ordernote.modify'



