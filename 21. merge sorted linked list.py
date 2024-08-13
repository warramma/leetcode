# tags: linkedlist
# time: O(n + m ) (size of both lists)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(math.inf)
        tail = dummy
        curr1 = list1
        curr2 = list2

        while True:
            if curr1 is None:
                tail.next = curr2
                break
            if curr2 is None:
                tail.next = curr1
                break
            if(curr1.val < curr2. val):
                temp = curr1
                curr1 = curr1.next
                #temp.next = tail.next
                tail.next = temp
            else:
                temp = curr2
                curr2 = curr2.next
                #temp.next = tail.next
                tail.next = temp
            
            tail = tail.next

        return dummy.next