# -*- coding: utf-8 -*-

'''

Created on 2018-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class FourpagedynamicdataQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.activityList = None
        self.memberNo = None
        
        self.setParamRule({
        	'memberNo':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryFourpagedynamicdata'

    def getApiMethod(self):

        return 'suning.online.fourpagedyna.query'



