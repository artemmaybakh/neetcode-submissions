# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head_1 = head
        head_2 = head
        
        if head.next is None:
            return
        
        for i in range(n-1):
            head_1 = head_1.next
                
        # print(head_1.val)   
        
        if head_1.next is None:
            head = head.next
        else:
            head_1 = head_1.next
            while head_1.next:
                head_1 = head_1.next
                head_2 = head_2.next
                # print(head_2.val, head_1.val)  
                

            head_2.next = head_2.next.next
        
        return head

                
 
        