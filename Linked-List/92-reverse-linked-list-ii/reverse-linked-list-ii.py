# LeetCode usually already provides this definition:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        # Move `prev` to the node just before position `left`
        for _ in range(left - 1):
            prev = prev.next

        # `curr` is the first node of the sublist to reverse
        curr = prev.next

        # Repeatedly take the node right after curr and move it to the front
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next