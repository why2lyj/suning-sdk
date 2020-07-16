# -*- coding: utf-8 -*-
'''
Created on 2014-5-27, Auto Generated 
@author: momo
'''
from suning.api.abstract import AbstractApiimport base64

class PicAddRequest(AbstractApi):
    '''
    '''
    def __init__(self):
        AbstractApi.__init__(self)        self.picContent = None
        def setFilePath(self,filepath):        image = open(filepath, 'rb')        imageData = image.read()        image.close()        imageData = base64.b64encode(imageData)        '''                              判断是否为字节  如果是字节需要转换为字符串        '''        if(isinstance(imageData, bytes)):            imageData =imageData.decode('utf-8')        LIMIT = 60        liIcon = []        while True:            sLimit = imageData[:LIMIT]            imageData = imageData[LIMIT:]            liIcon.append('\'%s\'' % sLimit)            if len(sLimit) < LIMIT:                break        self.picContent = ''.join(liIcon)        print(self.picContent)    
    def getApiBizName(self):
        return 'pic'

    def getApiMethod(self):
        return 'suning.custom.pic.add'

