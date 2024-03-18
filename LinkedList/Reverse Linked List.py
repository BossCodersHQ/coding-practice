from list_node import ListNode
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr.next:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return curr
    
if __name__ == "__main__":
    # test reverseList
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol = Solution()
    reversed_head = sol.reverseList(head)
    assert(reversed_head.val == 5)