# -*- coding: utf-8 -*-

'''

Created on 2015-10-28

@author: suning

'''

from suning.api.abstract import AbstractApi



class PackageOrderDeliverAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.packageOrderId = None
        self.deliveryType = None
        self.expressCompanyCode = None
        self.expressNo = None
        
        self.setParamRule({
        	'packageOrderId':{'allow_empty':False},
        	'deliveryType':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addPackageOrderDeliver'

    def getApiMethod(self):

        return 'suning.custom.packageorderdeliver.add'



