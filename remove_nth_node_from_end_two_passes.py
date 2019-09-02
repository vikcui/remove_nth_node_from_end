# author: YANG CUI
"""
Given a linked list, remove the n-th node from the end of list
and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list
becomes 1->2->3->5.

Two passes approach
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def romoveNthFromEnd(head, n):
    """
    :param head: the head of the listed list
    :param n: specifies which item to delete from the end
    :return: the head of the new linked list
    :time complexity: O(T) T being the total number of elements
    """
    lengthOfList = 0
    current = head
    # comute the length of the given linked list
    while current is not None:
        current = current.next
        lengthOfList += 1
    # compute the index from head to delete
    positionFromHead = lengthOfList - n
    if positionFromHead == 0:
        if lengthOfList != 0:
            return head.next
        else:
            return None
    current = head
    index = 0
    while index < positionFromHead - 1:
        current = current.next
        index += 1
    current.next = current.next.next
    return head

# l = ListNode(1)
# l.next = ListNode(2)
# l.next.next = ListNode(3)
# l.next.next.next = ListNode(4)
# l.next.next.next.next = ListNode(5)
#
# print(romoveNthFromEnd(l, 2))





