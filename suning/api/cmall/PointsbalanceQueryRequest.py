# -*- coding: utf-8 -*-

'''

Created on 2017-6-30

@author: suning

'''

from suning.api.abstract import AbstractApi



class PointsbalanceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.custNum = None
        
        self.setParamRule({
        	'custNum':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryPointsbalance'

    def getApiMethod(self):

        return 'suning.cmall.pointsbalance.query'



