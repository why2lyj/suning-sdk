# -*- coding: utf-8 -*-
"""
包含字符串常用工具  为兼容python2.x 和python3.x的字符串处理
Created on 2014年5月29日
@author: momo
"""


class StringUtils(object):
    """
    目前仅包含dict转string函数
    """

    def __init__(self, string=''):
        self.string = string

    def dict2string(self, dict_d):
        """
        dict转string，支持中文,支持dict多层嵌套，支持嵌套list
        @param dict_d: 传入的dict
        """
        self.string = self.__parseDict__(dict_d)
        return self.string
    
    ''' 
        add by 14050313 at 20140603
    '''                    
    def __parseDict__(self, dict_a):   
        tempString = ''                 
        num=0
        for t in dict_a.keys():
            num+=1
            tempvalue = dict_a[t]
            if isinstance(tempvalue, dict):
                tempdstring=self.__parseDict__(tempvalue)
                fill = '"%s":%s'%(t,tempdstring)
                tempString+=fill
            elif isinstance(tempvalue, list):
                tempdstring = self.__parseList__(tempvalue)
                fill = '"%s":[%s]'%(t,tempdstring)
                tempString+=fill    
            else:    
                fill = '"%s":"%s"'%(t,dict_a[t])
                tempString += fill
            if num!=len(dict_a):
                tempString +=','
        return '{%s}'%tempString        
    
    def __parseList__(self,list_a):
        tempString = ''
        num=0
        if isinstance(list_a, list):
            len_l = len(list_a)
            for inx in range(len_l):
                num+=1
                templistvalue=list_a[inx]
                if isinstance(templistvalue, dict):
                    tempString+=self.__parseDict__(templistvalue)
                else:
                    tempString+='"%s"'%templistvalue
                    
                if num!=len_l:
                    tempString+=','    
            return tempString           