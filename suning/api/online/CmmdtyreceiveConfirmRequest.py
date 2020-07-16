# -*- coding: utf-8 -*-

'''

Created on 2018-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtyreceiveConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderItemInfo = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'confirmCmmdtyreceive'

    def getApiMethod(self):

        return 'suning.online.cmmdtyreceive.confirm'



