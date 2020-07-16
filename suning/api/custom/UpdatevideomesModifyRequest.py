# -*- coding: utf-8 -*-

'''

Created on 2018-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class UpdatevideomesModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.channelid = None
        self.duration = None
        self.msg = None
        self.transcode = None
        self.widthheight = None
        self.imgurl = None
        
        self.setParamRule({
        	'channelid':{'allow_empty':False},
        	'duration':{'allow_empty':False},
        	'msg':{'allow_empty':False},
        	'transcode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyUpdatevideomes'

    def getApiMethod(self):

        return 'suning.custom.updatevideomes.modify'



