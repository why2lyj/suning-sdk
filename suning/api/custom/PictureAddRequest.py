# -*- coding: utf-8 -*-

'''

Created on 2020-4-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class PictureAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.content = None
        self.fileName = None
        self.mimeType = None
        
        self.setParamRule({
        	'content':{'allow_empty':False},
        	'fileName':{'allow_empty':False},
        	'mimeType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addPicture'

    def getApiMethod(self):

        return 'suning.custom.picture.add'



