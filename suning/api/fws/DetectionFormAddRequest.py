# -*- coding: utf-8 -*-

'''

Created on 2015-6-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class DetectionFormAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.qtOrderCode = None
        self.orderDetailId = None
        self.itemCode = None
        self.itemName = None
        self.itemDesc = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addDetectionForm'

    def getApiMethod(self):

        return 'suning.fws.detectionform.add'



