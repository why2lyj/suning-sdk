# -*- coding: utf-8 -*-

'''

Created on 2019-9-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class VideobatchReceiveRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.source = None
        self.type = None
        self.videoList = None
        self.videoType = None
        
        self.setParamRule({
        	'source':{'allow_empty':False},
        	'type':{'allow_empty':False},
        	'videoType':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'receiveVideobatch'

    def getApiMethod(self):

        return 'suning.custom.videobatch.receive'



