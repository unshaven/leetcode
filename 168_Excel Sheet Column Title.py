
# -*- coding: utf-8 -*-

#author :wuji
#data:2018-2-2
#difficulty degree：
#problem: 168_Excel Sheet Column Title
#time_complecity:  
#space_complecity: 
#beats: 
'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''
#与求二进制相似，一种方法可以用递归，还可以用while循环
class Solution():
    def convertToTitle(self, n):
    """
    :type n: int
    :rtype: str
    """
    #递归
    if n == 0:
        return ""
    else:
        return self.convertToTitle(int((n-1/26)))+chr(ord('A'+int((n-1)/%26)))
    def convertToTitle2(self, n):
    """
    :type n: int
    :rtype: str
    """
    #循环
    L = []
    while n > 0:
        n -= 1
        L.insert(0,chr(ord('A')+int((n-1)%26)))
        n = int(n/26)
    return ''.join(L)        # 比如 [1,2,3,4] 可以变成1234
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                                                      
            
    
