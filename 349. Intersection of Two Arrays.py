'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.

'''
class Solution:
      def intersection1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1&nums2)     set()求交集 求合集| 
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = {}
        l = []
        for num1 in nums1:
            result[num1] = True
        for num2 in nums2:
            if num2 in result.keys():
                if num2 not in l:
                    l.append(num2)
        return l
      
