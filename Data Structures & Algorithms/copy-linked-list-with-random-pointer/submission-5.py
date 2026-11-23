"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        head_1 = head
        copies = {}
        while head_1:
            copies[head_1] = Node(head_1.val)
            head_1 = head_1.next
            
        head_1 = head 
        while head_1:

            copies[head_1].next = copies.get(head_1.next)
            copies[head_1].random = copies.get(head_1.random)
            head_1 = head_1.next
            
        head_1 = head 
        
        return copies.get(head)