# -*- coding: utf-8 -*-

'''

Created on 2015-6-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class DetectionFormDeleteRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.qtOrderCode = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'deleteDetectionForm'

    def getApiMethod(self):

        return 'suning.fws.detectionform.delete'



