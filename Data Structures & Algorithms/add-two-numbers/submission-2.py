# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:     
        summa = 0 
        pre_l3 = None
        if l1 is None:
                return l2
        if l2 is None:
            return l1
        summa += l1.val + l2.val 
        l3 = ListNode(summa % 10, pre_l3)
        res = l3
        pre_l3 = l3
        l2 = l2.next
        l1 = l1.next
        summa = summa // 10
        
        while l1 or l2 or summa:
            if l1:
                summa += l1.val
                l1 = l1.next
                
            if l2:
                summa += l2.val
                l2 = l2.next
            l3 = ListNode(summa % 10, None)
            pre_l3.next = l3
            pre_l3 = pre_l3.next

            summa = summa // 10
            
        return res

        