# -*- coding: utf-8 -*-

#author :wuji
#data:2018-2-1
#difficulty degree：
#problem: 141_linked list cycle
#time_complecity:  
#space_complecity: 
#beats: 
'''
Given a linked list, determine if it has a cycle in it.
Follow up:
Can you solve it without using extra space?
'''
#可以用快慢指针的方法，慢指针每次走一步，快指针每次走两步，如果存在环，两者必相遇

class TreeNode(object):
    def __init__(self,x):
      self.val = x
      self.next = None
    
class Solution():
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        slow = head
        fast = head
        while fast != None and fast.next != None:
          slow = slow.next
          fast = fast.next.next
          if fast == slow:
            return True
        return False
          #reverse
    #反转链表，将走过的路径进行反转。
    #若有环，则会从环入口那里回到head处，若没有环，则会到终点处，不会回到head处。
    def hasCycle2(self, head):
        pre, cur = None, head
        while cur:
            pre, cur.next, cur = cur, pre, cur.next
            if cur == head: return True
        return False
      
      
      
    def hasCycle2(self,head):              #循环的方法反转链表  
        if head is None or head.next is None:  
            return head;  
        pre=None;  
        cur=head;  
        h=head;  
        while cur:  
            h=cur;  
            tmp=cur.next;  
            cur.next=pre;  
            pre=cur;  
            cur=tmp;  
        return h;  
