# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return
        
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        head_1 = head
        head_2 = slow.next
        slow.next = None
        rev_head = None
        while head_2:
            next_head = head_2.next
            head_2.next = rev_head
            rev_head = head_2
            head_2 = next_head
        
        new_head = head
        while rev_head and new_head:
            next_rev_head = rev_head.next
            next_new_head = new_head.next
            
            new_head.next = rev_head
            new_head = new_head.next
            
            new_head.next = next_new_head
            new_head = new_head.next
            rev_head = next_rev_head
                   
        