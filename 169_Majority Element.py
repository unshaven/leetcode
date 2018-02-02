# -*- coding: utf-8 -*-

#author :wuji
#data:2018-2-2
#difficulty degree：
#problem: 169_Majority Element
#time_complecity:  
#space_complecity: 
#beats: 
'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''
#字典
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if dic.get(i) is None:
                dic[i] = 1
            else:
                dic[i] += 1
            if dic[i] > int(len(nums)/2):
                return i
    # 一次循环 由于只需要找到出现次数大于n/2的，就是出现次数最多的数
    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        major = nums[0]
        for i in range(1,len(nums)):
            if count == 0:
                count += 1
                major = nums[i]
            elif nums[i] == major:
                count += 1
            else:
                count -= 1  
        return major
    # 出现次数大于n/2 必定nums[len(nums)/2]是所求值
    def majorityElement3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()   #改变了nums
        return nums[int(len(nums)/2)]
        
                
                
                
                
        
