from typing import Optional

from list_node import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid point and seperate lists
        def get_second_list(node):
            first_ptr = second_ptr = node
            while second_ptr.next and second_ptr.next.next:
                first_ptr = first_ptr.next
                second_ptr = second_ptr.next.next
            second_list = first_ptr.next
            first_ptr.next = None
            return second_list

        def reverse(node):
            prev = None
            curr = node
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        def merge(l1, l2):
            sentinal = curr = ListNode()
            while l1 and l2:
                curr.next = l1
                l1 = l1.next
                curr = curr.next

                curr.next = l2
                l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return sentinal.next

        first_list = head
        second_list = get_second_list(first_list)
        second_list = reverse(second_list)
        merge(first_list, second_list)


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s.reorderList(head)
    assert head.to_list() == [1, 5, 2, 4, 3]

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    s.reorderList(head)
    assert head.to_list() == [1, 4, 2, 3]

    head = ListNode(1, ListNode(2, ListNode(3)))
    s.reorderList(head)
    assert head.to_list() == [1, 3, 2]

    head = ListNode(1, ListNode(2))
    s.reorderList(head)
    assert head.to_list() == [1, 2]

    head = ListNode(1)
    s.reorderList(head)
    assert head.to_list() == [1]
