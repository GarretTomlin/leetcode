# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head
        
        current, prev = head, None
        i = 1  

        while current is not None and i < left:
            prev = current
            current = current.next
            i += 1

        last_node = prev
        last_node_list = current
        
        while current is not None and i <= right:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            i += 1

        if last_node is not None:
            last_node.next = prev
        else:
            head = prev

        last_node_list.next = current

        return head
