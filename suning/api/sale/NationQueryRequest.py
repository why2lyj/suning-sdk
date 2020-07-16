# -*- coding: utf-8 -*-

'''

Created on 2014-5-27, Auto Generated 

@author: momo

'''

from suning.api.abstract import AbstractApi



class NationQueryRequest(AbstractApi):

    '''
        国家代码查询<br>其他业务类和此类结构相同，此文档不再列举
    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.nationName = None



    def getApiBizName(self):

        return 'nation'



    def getApiMethod(self):

        return 'suning.custom.nation.query'



