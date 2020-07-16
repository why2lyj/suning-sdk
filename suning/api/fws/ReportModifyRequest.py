# -*- coding: utf-8 -*-

'''

Created on 2019-8-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReportModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.described = None
        self.fileName = None
        self.isPass = None
        self.itemCode = None
        self.itemDesc = None
        self.itemName = None
        self.memo = None
        self.orderDetailId = None
        self.productLink = None
        self.qtCode = None
        self.qtExpiry = None
        self.qtFile = None
        self.qtOrderCode = None
        self.qtOrderStatus = None
        self.qtStandard = None
        self.qtType = None
        
        self.setParamRule({
        	'isPass':{'allow_empty':False},
        	'itemCode':{'allow_empty':False},
        	'itemName':{'allow_empty':False},
        	'orderDetailId':{'allow_empty':False},
        	'qtCode':{'allow_empty':False},
        	'qtOrderCode':{'allow_empty':False},
        	'qtOrderStatus':{'allow_empty':False},
        	'qtType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyReport'

    def getApiMethod(self):

        return 'suning.fws.report.modify'



