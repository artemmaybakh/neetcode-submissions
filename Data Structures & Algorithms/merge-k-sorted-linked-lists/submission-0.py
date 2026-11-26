# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is not None and lists: 
            while len(lists) > 1:
                cur_list = []
                for i in range(0, len(lists) - 1, 2):
                    cur_list.append(self.mergeTwoLists(lists[i], lists[i+1]))
                    
                if len(lists) % 2 != 0:
                    cur_list.append(lists[-1])  
                
                lists  = cur_list[:]
                
            return lists[0]
        return None

    def mergeTwoLists(self, l1: List[Optional[ListNode]], l2: List[Optional[ListNode]]):
        l3 = None
        
        if l1 and l2:
            if l1.val < l2.val:
                l3 = l1
                l1 = l1.next
            else:
                l3 = l2
                l2 = l2.next
                
        elif l1:
            l3 = l1
            l1 = l1.next
        elif l2:
            l3 = l2
            l2 = l2.next
            
        res = l3
                
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    l3.next = l1
                    l1 = l1.next
                else:
                    l3.next = l2
                    l2 = l2.next
            elif l1:
                l3.next = l1
                l1 = l1.next
            elif l2:
                l3.next = l2
                l2 = l2.next
                
            l3 = l3.next
            
        return res
        
        
        