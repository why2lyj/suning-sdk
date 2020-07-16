# -*- coding: utf-8 -*-

'''

Created on 2019-2-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtybycouponoractQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityId = None
        self.chanId = None
        self.city = None
        self.couponRuleId = None
        self.cp = None
        self.kw = None
        self.price = None
        self.ps = None
        self.snfw = None
        self.st = None
        self.stock = None
        self.type = None
        
        self.setParamRule({
        	'chanId':{'allow_empty':False},
        	'city':{'allow_empty':False},
        	'cp':{'allow_empty':False},
        	'ps':{'allow_empty':False},
        	'snfw':{'allow_empty':False},
        	'type':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCmmdtybycouponoract'

    def getApiMethod(self):

        return 'suning.online.cmmdtybycouponoract.query'



