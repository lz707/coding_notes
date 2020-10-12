# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #add each Node from L1 and L2, consider when one of them is None
        #if sum >10 then add round(sum/10) to to next sum
        
        num = l1.val + l2.val
        e = num % 10
        n = num//10
        l3 = ListNode(val=e)
        l1_ = l1.next
        l2_ = l2.next
        l3_ = l3
        while l1_ is not None or l2_ is not None:
            if l1_ is not None and l2_ is not None:
                num = l1_.val + l2_.val + n
                l1_ = l1_.next
                l2_ = l2_.next
            elif l1_ is not None and l2_ is None:
                num = l1_.val + n
                l1_ = l1_.next
            elif l2_ is not None and l1_ is None:
                num = l2_.val + n
                l2_ = l2_.next
                
            e = num % 10
            n = num//10
            element = ListNode(val=e)
            l3_.next = element
            l3_= l3_.next
            
        if n == 1:
            element = ListNode(val=n)
            l3_.next = element 
            
        return l3
