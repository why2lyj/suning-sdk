# -*- coding: utf-8 -*-

'''

Created on 2014-9-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class ComphandleGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.complaintCode = None



    def getApiBizName(self):

        return 'getComplaintHandle'



    def getApiMethod(self):

        return 'suning.custom.comphandle.get'



