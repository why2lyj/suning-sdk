# -*- coding: utf-8 -*-

'''

Created on 2014-9-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class ComplaintGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.complaintCode = None
        self.orderCode = None



    def getApiBizName(self):

        return 'getComplaint'



    def getApiMethod(self):

        return 'suning.custom.complaint.get'



