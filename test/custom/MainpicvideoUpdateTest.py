#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-10-15

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.MainpicvideoUpdateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.picUrlEight='https://uimgpre.cnsuning.com/uimg/sop/commodity/380701634471150317364639_x.jpg'
a.picUrlFive='https://uimgpre.cnsuning.com/uimg/sop/commodity/380701634471150317364639_x.jpg'
a.picUrlFour='https://uimgpre.cnsuning.com/uimg/sop/commodity/380701634471150317364639_x.jpg'
a.picUrlNine='https://uimgpre.cnsuning.com/uimg/sop/commodity/380701634471150317364639_x.jpg'
a.picUrlOne='https://uimgpre.cnsuning.com/uimg/sop/commodity/380701634471150317364639_x.jpg'
a.picUrlSeven='https://uimgpre.cnsuning.com/uimg/sop/commodity/380701634471150317364639_x.jpg'
a.picUrlSix='https://uimgpre.cnsuning.com/uimg/sop/commodity/380701634471150317364639_x.jpg'
a.picUrlTen='https://uimgpre.cnsuning.com/uimg/sop/commodity/380701634471150317364639_x.jpg'
a.picUrlThree='https://uimgpre.cnsuning.com/uimg/sop/commodity/380701634471150317364639_x.jpg'
a.picUrlTwo='https://uimgpre.cnsuning.com/uimg/sop/commodity/380701634471150317364639_x.jpg'
a.productCode='100024868'
a.supplierCode='70076688'
a.videoCode='1630383'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)