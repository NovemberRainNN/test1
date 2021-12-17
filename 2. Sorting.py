# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 09:45:56 2021

@author: lixin
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def merge2Lists(self, l1, l2):
            head = point = ListNode(0)
            while l1 and l2:
                if l1.val <= l2.val:
                    point.next = l1
                    l1 = l1.next
                else:
                    point.next = l2
                    l2 = l1  # 指针互相指
                    l1 = point.next.next
                point = point.next
            if not l1:
                point.next=l2
            else:
                point.next=l1
            return head.next

l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
 
l2 = ListNode(2)
l2.next = ListNode(6)
# l = ListNode()
# l.merge2Lists(l1,l2)
l2 = l1
print(l2.next.val)