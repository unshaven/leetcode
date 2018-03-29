'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

'''
学习一种新的方法 Counter容器
from collections impoet Counter
例如[1,1,1,2,2,3]
Counter([1,1,1,2,2,3]) = {1:3,2:2,3:1}
class Solution(object):
    def intersect1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        return list((c1&c2).elements())     list(Counter.elements) 是把{1:3,2:2,3:1}变成[1,1,1,2,2,3]
    def intersect2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            tmp = nums1
            nums1 = nums2
            nums2 = tmp
        result = {}
        l = []
        for index,value in enumerate(nums1):
            result[value] = result.get(value,0)+1            等价于计算一个list有多少个相同的元素{1:2,2:3}....
        for num2 in nums2:
            if num2 in result.keys():
                if result[num2] == 0:
                    continue
                result[num2] -= 1
                l.append(num2)
        return l
