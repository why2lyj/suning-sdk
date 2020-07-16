# -*- coding: utf-8 -*-

'''

Created on 2020-4-13

@author: suning

'''

from suning.api.abstract import AbstractApi



class PictureDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.objectId = None
        
        self.setParamRule({
        	'objectId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'deletePicture'

    def getApiMethod(self):

        return 'suning.custom.picture.delete'



