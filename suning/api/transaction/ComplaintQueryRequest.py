# -*- coding: utf-8 -*-

'''

Created on 2014-9-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class ComplaintQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.complaintStatus = None
        self.startTime = None
        self.endTime = None
        self.pageNo = None
        self.pageSize = None



    def getApiBizName(self):

        return 'queryComplaint'



    def getApiMethod(self):

        return 'suning.custom.complaint.query'



