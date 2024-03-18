from typing import Optional
from list_node import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        from collections import defaultdict
        map = defaultdict(int)
        curr = head
        while curr:
            map[curr] += 1
            if map[curr] > 1:
                return True
            curr = curr.next
        return False
	
    def hasCyclePointers(self, head: Optional[ListNode]) -> bool:
        slow_ptr = fast_ptr = head
        while fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next if fast_ptr.next else None
            if slow_ptr == fast_ptr and slow_ptr != None:
                return True
        return False
    

if __name__ == "__main__":
    # test hasCycle
    head = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
    head.next.next.next.next = head.next
    sol = Solution()
    assert(sol.hasCycle(head) == True)
    assert(sol.hasCyclePointers(head) == True)
    head.next.next.next.next = None
    assert(sol.hasCycle(head) == False)
    assert(sol.hasCyclePointers(head) == False)
    print("all tests passed.")