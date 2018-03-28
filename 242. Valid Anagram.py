'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

'''

#题目的意思是打乱字母的顺序重新排列就是True
最简单的方法是 直接用sorted()函数
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
    第二种就是用Hash 会使用dict.get(,default)
    def isAnagram2(self,s,t):
        result1 = {}
        result2 = {}
        for s1 in s:
          result1[s1] = result1.get(s1,0) + 1
        for t1 in t:
          result2[t1] = result2.get(t1,0) + 1
        return result1 == result2
