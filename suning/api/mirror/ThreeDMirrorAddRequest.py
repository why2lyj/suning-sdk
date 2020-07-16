# -*- coding: utf-8 -*-

'''

Created on 2016-5-27

@author: suning

'''

from suning.api.abstract import AbstractApi



class ThreeDMirrorAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.productCode = None
        self.zipContent = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False},
        	'zipContent':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addThreeDMirror'

    def getApiMethod(self):

        return 'suning.mirror.threedmirror.add'



