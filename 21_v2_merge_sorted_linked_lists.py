'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''
#given the heads of two SORTED linked lists!
def Node():
    def __init__ (self, value = 0, next = None):
        self.val = value
        self.next = next

def mergeTwoLists(list1, list2):
    #drawing a picture helps!
    #use a temp node, and a previous pointer to keep track of where you are in the new list
    #if preserving original lists, use pointers instead of the given heads

    temp = Node()
    previous = temp
    pointer_one = list1
    pointer_two = list2

    while pointer_one or pointer_two:
        if not pointer_one:
            previous.next = pointer_two
            pointer_two = pointer_two.next
            previous = previous.next
            continue
        if not pointer_two:
            previous.next = pointer_one
            pointer_one = pointer_one.next
            previous = previous.next
            continue
        
        if pointer_one.val < pointer_two.val:
            previous.next = pointer_one
            pointer_one = pointer_one.next
            previous = previous.next
        else:
            previous.next = pointer_two
            pointer_two = pointer_two.next
            previous = previous.next

    return temp.next