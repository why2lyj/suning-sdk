# coding=UTF-8
'''
Created on 2016年2月22日

@author: 15051125
'''
from suning.messagePush import messagePush
from suning.messagePush import message

    
if __name__ == "__main__":
    mess = message.Message()
    # p=messagePush.WebSocketClient("ws://10.27.132.215:9527/websocket","924b40606b7bd319eeb43d4a4c25fb6c","d04ec32f43e47e1286f258bd3ec5f721","default1")
    p=messagePush.WebSocketClient("wss://mcsit.api.cnsuning.com/websocket","924b40606b7bd319eeb43d4a4c25fb6c","d04ec32f43e47e1286f258bd3ec5f721","default1")
    p.connect()
    mess = p.onMessage()
    while mess != None:
        print(mess.getMessageId())
        mess = p.onMessage()

