# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next

        stack_len = len(stack)
        target_i = stack_len-n

        if target_i==0:
            head = head.next
        else:
            if target_i+1<stack_len:
                pre_node = stack[target_i-1]
                next_node = stack[target_i+1]
                pre_node.next = next_node
            else:
                pre_node = stack[target_i-1]
                pre_node.next = None


        return head