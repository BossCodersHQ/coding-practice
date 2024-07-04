from list_node import ListNode
from typing import Optional, List


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2lists(
            lst1: Optional[ListNode], lst2: Optional[ListNode]
        ) -> Optional[ListNode]:
            head = curr = ListNode(0)

            while lst1 and lst2:
                if lst1.val < lst2.val:
                    curr.next = lst1
                    curr = curr.next
                    lst1 = lst1.next
                else:
                    curr.next = lst2
                    curr = curr.next
                    lst2 = lst2.next
            if not lst1:
                curr.next = lst2
            else:
                curr.next = lst1

            return head.next

        if len(lists) == 0:
            return
        while len(lists) > 1:
            lst1 = lists[-1]
            lst2 = lists[-2]
            new_lst = merge2lists(lst1, lst2)
            lists.pop()
            lists.pop()
            lists.append(new_lst)

        return lists[0]


if __name__ == "__main__":
    s = Solution()

    # Test case 1
    lst1 = ListNode(1)
    lst1.next = ListNode(4)
    lst1.next.next = ListNode(5)

    lst2 = ListNode(1)
    lst2.next = ListNode(3)
    lst2.next.next = ListNode(4)

    lst3 = ListNode(2)
    lst3.next = ListNode(6)

    result = s.mergeKLists([lst1, lst2, lst3])

    while result:
        print(result.val)
        result = result.next

    # Test case 2
    lst1 = None
    lst2 = None
    lst3 = None

    result = s.mergeKLists([lst1, lst2, lst3])
    while result:
        print(result.val)
        result = result.next
