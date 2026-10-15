# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None or k==0 or not head.next:
            return head
        l=1
        tail=head
        while tail.next:
            tail=tail.next
            l+=1
        k=k%l
        if k==0:
            return head
        tail.next=head
        steps=l-k
        new_tail=head
        for _ in range(steps-1):
            new_tail=new_tail.next
        head=new_tail.next
        new_tail.next=None
        return head
