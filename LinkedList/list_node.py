#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result