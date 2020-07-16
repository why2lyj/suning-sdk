# -*- coding: utf-8 -*-

'''

Created on 2019-5-29

@author: suning

'''

from suning.api.abstract import AbstractApi



class VedioModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.classifyName = None
        self.source = None
        self.type = None
        self.videoCode = None
        self.videoId = None
        self.videoName = None
        self.videoSize = None
        self.videoSizeKb = None
        self.videoUrlId = None
        self.videoUrlTv = None
        
        self.setParamRule({
        	'type':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyVedio'

    def getApiMethod(self):

        return 'suning.custom.vedio.modify'



