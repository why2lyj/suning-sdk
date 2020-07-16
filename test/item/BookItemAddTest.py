#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014年6月5日

@author: dd

文化制品类商品增加
'''
import sys
sys.path.append("../../../api-sdk-python")

import suning.api as api

a = api.BookItemAddRequest()
a.invQty = "1"
a.saleCatalogCode = "226412"
a.price = "10.00"
a.brandCode = "00BC"
a.productName = u"你好中国123"
a.itemCode = "111111"
a.categoryCode = "R5101006"
a.pars = [{"parCode": "cmBarcode","parValue": "9787510447327"},
          {"parCode": "grossWeight","parValue": "978.7"},
          {"parCode": "volume","parValue": "9.7"},
          {"parCode": "insert_pic1","parValue": "http://10.19.95.100/uimg/sop/commodity/201406061108432112_x.jpg"},
          {"parCode": "insert_pic2","parValue": "http://10.19.95.100/uimg/sop/commodity/201406061108432112_x.jpg"},
          {"parCode": "insert_pic3","parValue": "http://10.19.95.100/uimg/sop/commodity/201406061108432112_x.jpg"},
          {"parCode": "insert_pic4","parValue": "http://10.19.95.100/uimg/sop/commodity/201406061108432112_x.jpg"},
          {"parCode": "insert_pic5","parValue": "http://10.19.95.100/uimg/sop/commodity/201406061108432112_x.jpg"},
          {"parCode": "editors_choice","parValue": "editors_choice"},
          {"parCode": "brief_intro","parValue": "brief_intro"},
          {"parCode": "about_author","parValue": "about_author"},
          {"parCode": "media_comm","parValue": "media_comm"},
          {"parCode": "directory","parValue": "directory"},
          {"parCode": "book_excerpt","parValue": "book_excerpt"}]
a.freightTemplateId = "81accea93b0747a090648b3ea1d42554"
a.saleSet = "1"
a.sellPoint = u"你好呢"
a.afterSaleServiceDec = "11111"
a.img1Url = "http://10.19.95.100/uimg/sop/commodity/201406061108432112_x.jpg"
#a.saleDate = ""
a.alertQty = "10"

try:
    print(a.getApiContent())
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)