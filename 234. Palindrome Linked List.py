'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''
#三种方法 最简单的是o(n)时间复杂度和o(n)的空间复杂度 定义一个list 一步一步往里面append

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#o(n)的时间复杂度  o(n/2)的空间复杂度,思路是找到单链表的中点,把前半段的Node放进List 然后与后半段比较
#找到linked list 的中点:
  def getMidOfListNode(head):
    fast=slow=head
    while fast and fast.next and fast.next.next:
      slow = slow.next
      fast = fast.next
#判断list是否奇数个:
  def isOdd(head):
    fast=slow=head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next
    if fast:  #奇数个
 
o(n)时间 o(1)空间
class Solution2:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        #用快慢指针的方法找到中点
        slow=fast=head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow = slow.next  #指向后半段的头部

        slow = self.reverseListNode(slow)
        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True
    def reverseListNode(self,head):
        new = None
        while head:
            p = head
            head = head.next
            p.next = new
            new = p
        return new
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

