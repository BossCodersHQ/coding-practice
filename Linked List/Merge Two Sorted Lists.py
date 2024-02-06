from list_node import ListNode
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if not list1 and list2:
            curr.next = list2
        elif list1 and not list2:
            curr.next = list1	
        return head.next
    
if __name__ == "__main__":
    # test mergeTwoLists
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    sol = Solution()
    merged = sol.mergeTwoLists(l1, l2)
    assert(merged.val == 1)
    assert(merged.next.val == 1)
    assert(merged.next.next.val == 2)
    assert(merged.next.next.next.val == 3)
    assert(merged.next.next.next.next.val == 4)
    assert(merged.next.next.next.next.next.val == 4)