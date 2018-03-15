
# -*- coding: utf-8 -*-

#author :wuji
#data:2018-3-15
#difficulty degree：
#problem: 720_Longest Word in Dictionary.py
#time_complecity:  
#space_complecity: 
#beats: 
'''
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
'''
#有几个比较常用的函数，sorted()可以从小到大排序，如果list中是字符串，也是按照字符串大小排列的
#还有一个max(,key=abs,len)是按照长度还是什么排序
class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        longest, l = '', {''}
        for word in sorted(words):
            if word[:-1] in l:
                l.add(word)
        return max(sorted(l),key=len)



















