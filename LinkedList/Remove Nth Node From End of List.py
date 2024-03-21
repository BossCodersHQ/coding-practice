from typing import List, Optional

from list_node import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Add sentinal node
        sentinal = frontptr = backptr = ListNode()
        sentinal.next = head

        # take first pointer n+1 spaces forward
        for i in range(n + 1):
            frontptr = frontptr.next

        # while frontptr: move both ptrs forward
        while frontptr:
            backptr = backptr.next
            frontptr = frontptr.next

        backptr.next = backptr.next.next
        return sentinal.next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert s.removeNthFromEnd(head, 2).to_list() == [1, 2, 3, 5]
    head = ListNode(1)
    assert s.removeNthFromEnd(head, 1) == None
    head = ListNode(1, ListNode(2))
    assert s.removeNthFromEnd(head, 1).to_list() == [1]
    head = ListNode(1, ListNode(2))
    assert s.removeNthFromEnd(head, 2).to_list() == [2]
    head = ListNode(1, ListNode(2, ListNode(3)))
    assert s.removeNthFromEnd(head, 1).to_list() == [1, 2]
    head = ListNode(1, ListNode(2, ListNode(3)))
    assert s.removeNthFromEnd(head, 2).to_list() == [1, 3]
    head = ListNode(1, ListNode(2, ListNode(3)))
    assert s.removeNthFromEnd(head, 3).to_list() == [2, 3]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    assert s.removeNthFromEnd(head, 1).to_list() == [1, 2, 3]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    assert s.removeNthFromEnd(head, 2).to_list() == [1, 2, 4]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    assert s.removeNthFromEnd(head, 3).to_list() == [1, 3, 4]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    assert s.removeNthFromEnd(head, 4).to_list() == [2, 3, 4]
