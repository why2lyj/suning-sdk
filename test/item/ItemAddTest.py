#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014年6月4日

@author: 14050313
'''
import sys
sys.path.append("../../../api-sdk-python")

import suning.api 

a=suning.api.ItemAddRequest()
''' 无子产品商品添加  begin  '''
a.brandCode = "A120"
a.categoryCode = "R3301006"
a.pars = [{"parCode": "cm_model","parValue": "LB1"},{"parCode": "cm_barCode","parValue": "1"},{"parCode": "BRGEW","parValue": "1"},{"parCode": "VOLUM","parValue": "0.2"},
          {"parCode": "country", "parValue": "CN"}, {"parCode": "region","parValue": "100"},{"parCode": "city", "parValue": "000001000173" }]
a.packingList = [{ "packingListName":"ff20140523","packingListQty":"1"}]
a.productName = "ff120140523"
a.freightTemplateId = "231b79eef3e84f899f27d4d962ffa975"
a.invQty = "1"
a.itemCode = '55667788'
a.img1Url = 'http://10.19.95.100/uimg/sop/commodity/201406051640108724_x.jpg'
a.img2Url = 'http://10.19.95.100/uimg/sop/commodity/201406051640108724_x.jpg'
a.img3Url = 'http://10.19.95.100/uimg/sop/commodity/201406051640108724_x.jpg'
a.img4Url = 'http://10.19.95.100/uimg/sop/commodity/201406051640108724_x.jpg'
a.img5Url = 'http://10.19.95.100/uimg/sop/commodity/201406051640108724_x.jpg'
a.saleSet = "0"
a.introduction = "5rWL6K+V5ZWG5ZOB5LuL57uN"
a.sellPoint = "ff20140523"
a.afterSaleServiceDec = "ff20140523"
a.price = "11"
a.saleDate = "2014-06-07"
try:
    print(a.getApiContent())
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)

''' 无子产品商品添加  end  '''
    
''' 含有子产品商品添加  begin  '''  
a=suning.api.ItemAddRequest() 
a.brandCode = "A120"
a.categoryCode = "R3301010"
a.packingList = [{ "packingListName":"ff20140523","packingListQty":"1"}]
a.productName = "ff11120140523"
a.freightTemplateId = "231b79eef3e84f899f27d4d962ffa975"
a.itemCode = '55667788'
a.pars = [{"parCode": "cm_model","parValue": "LB1"},{"parCode": "cm_barCode","parValue": "1"},{"parCode": "BRGEW","parValue": "1"},{"parCode": "VOLUM","parValue": "0.2"},
          {"parCode": "country", "parValue": "CN"}, {"parCode": "region","parValue": "100"},{"parCode": "city", "parValue": "000001000173" }]
a.childItem = [{"barcode": "212",
               "img1Url": "http://10.19.95.100/uimg/sop/commodity/201406051640108724_x.jpg", "img2Url": "http://10.19.95.100/uimg/sop/commodity/201406051640108724_x.jpg",
               "img3Url": "http://10.19.95.100/uimg/sop/commodity/201406051640108724_x.jpg", "img4Url": "http://10.19.95.100/uimg/sop/commodity/201406051640108724_x.jpg",
               "img5Url": "http://10.19.95.100/uimg/sop/commodity/201406051640108724_x.jpg",
               "invQty": "1","itemCode": "445212",
               "pars": [{"parCode": "G99001", "parValue": "11" }],
               "price": "10.23"
             }]
a.saleSet = "0"
a.introduction = "5rWL6K+V5ZWG5ZOB5LuL57uN"
a.sellPoint = "ff20140523"
a.afterSaleServiceDec = "ff20140523"
a.saleDate = "2014-06-07"
try:
    print(a.getApiContent())
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)     
''' 含有子产品商品添加  end  '''
    