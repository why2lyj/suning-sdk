#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2019-12-13

@author: suning
'''
import sys
import os
basepath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../"
sys.path.append(basepath)

import suning.api as api

a=api.AppointCreateRequest()

a.setDomainInfo("openpre.cnsuning.com","80")
a.setAppInfo("a13b8bd0efb06a770c57d1c370ce8ee7", "f08ce9836c4bcfc708194594081f6690")
# 如果使用oauth认证方式，那么调用下面方法来添加accessToken
#a.setAccessToken("4caf7fa30dd8")
a.actionEndTime='2019-10-01 00:00:01'
a.actionId='2019102800001'
a.actionName='预约活动名称'
a.actionStartTime='2019-10-01 00:00:01'
a.actionType='0:普通预约'
a.adapteTerminal='1：PC，2：移动，3：PC+移动'
a.enrollInfoCode='SU191028101810140135'
a.excludeCitys='9017,9264'
a.goodsList=[{"priceLabel":"3？？9","personBuyLimit":"2","partnumber":"000000000123456789","price":"3899","standard":"42码","color":"红色","partName":"这是商品名称","msgContent":"您好，您预约的XXX将于XXX开始抢购......","catengrpCode":"000000000123456788","appointPrice":"3999","totalLimit":"10000","defaultGoodsFlags":"1"}]
a.goodsSubList=[{"count":"2","subPartName":"这是子商品名称","subPartNumber":"000000000123456789","subAppointPrice":"500","subPrice":"399","subTextPrice":"299"}]
a.noticePhone='11111111111'
a.operateType='01：新建，02：修改，03：停用'
a.operateUser='工号'
a.otherTerminalSale='0：否，1：是'
a.partType='00：普通单商品，01：通子码商品，02：蔟商品，03：套餐商品'
a.phoneShareContent='***商品正在做预约'
a.phoneShareImgUrl='url链接'
a.phoneShareTitle='我在苏宁易购预约了商品'
a.phoneShareUrl='url链接'
a.purchaseEndTime='2019-10-01 00:00:01'
a.purchaseStartTime='2019-10-01 00:00:01'
a.receiveSys='AAAA'
a.scheduleEndTime='2019-10-01 00:00:01'
a.scheduleStartTime='2019-10-01 00:00:01'
a.sendScalperMsg='0：不发送，1：发送'
a.sendUserMsg='0：不发送，1：发送'
a.supervipPurchaseStartTime='2019-10-01 00:00:01'
a.ticketResaleStartTime='2019-10-01 00:00:01'
a.transitDate='2019-10-01 00:00:01'
a.transitFlag='2:否，1:是'
a.vendorCode='0000000000'
a.vendorName='商家名称'
a.vendorType='00-自营,10-代表C模式,20-代表SWL模式,30-代表海外购模式,50-线上联营'
a.versionNumber='1'

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)