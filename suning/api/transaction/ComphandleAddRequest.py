# -*- coding: utf-8 -*-

'''

Created on 2014-9-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class ComphandleAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.complaintCode = None
        self.handleType = None
        self.handleText = None



    def getApiBizName(self):

        return 'addComplaintHandle'



    def getApiMethod(self):

        return 'suning.custom.comphandle.add'



