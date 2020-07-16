# -*- coding: utf-8 -*-

'''

Created on 2019-10-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class MainpicvideoUpdateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.picUrlEight = None
        self.picUrlFive = None
        self.picUrlFour = None
        self.picUrlNine = None
        self.picUrlOne = None
        self.picUrlSeven = None
        self.picUrlSix = None
        self.picUrlTen = None
        self.picUrlThree = None
        self.picUrlTwo = None
        self.productCode = None
        self.supplierCode = None
        self.videoCode = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False},
        	'videoCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'updateMainpicvideo'

    def getApiMethod(self):

        return 'suning.custom.mainpicvideo.update'



