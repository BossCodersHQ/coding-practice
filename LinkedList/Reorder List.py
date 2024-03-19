from typing import Optional
from list_node import ListNode
class Solution:
	def reorderList(self, head: Optional[ListNode]) -> None:
		def find_mid(node):
			slow_ptr = fast_ptr = node
			while fast_ptr.next and fast_ptr.next.next:
				slow_ptr = slow_ptr.next
				fast_ptr = fast_ptr.next.next
			return slow_ptr
		
		mid = find_mid(head)
		new_head = mid.next
		mid.next = None
		
		def merge(l1,l2):
			sentinal = ListNode()
			tail = sentinal
			while l1 and l2:
					tail.next = l1
					l1 = l1.next
					tail = tail.next
					
					tail.next = l2
					l2 = l2.next
					tail = tail.next
			
			tail.next = l1 or l2
			return sentinal.next
		
		merge(head, new_head)
		
if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s.reorderList(head)
    assert head.to_list() == [1,5,2,4,3]
    
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    s.reorderList(head)
    assert head.to_list() == [1,4,2,3]
    
    head = ListNode(1, ListNode(2, ListNode(3)))
    s.reorderList(head)
    assert head.to_list() == [1,3,2]
    
    head = ListNode(1, ListNode(2))
    s.reorderList(head)
    assert head.to_list() == [1,2]
    
    head = ListNode(1)
    s.reorderList(head)
    assert head.to_list() == [1]
    
    head = None
    s.reorderList(head)
    assert head == None