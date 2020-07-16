#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014-9-25

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.OrderevalQueryRequest()

a.startTime='2014-9-10'
a.endTime='2014-9-20'
a.reviewLevel='123'
a.suplReviewFlag='1'
a.replyOrNot='12'
a.pageNo='123'
a.pageSize='1'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)