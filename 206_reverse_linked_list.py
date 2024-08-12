#206. reverse linked list
#tags: linkedlist
#date: 8-12-24
#difficulty: easy
#time complexity: O(n)
#space complexity: O(1)
#------------------------------------------------------------


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while(current):
            temp = current.next
            current.next = previous
            previous = current
            current = temp
    
        return previous