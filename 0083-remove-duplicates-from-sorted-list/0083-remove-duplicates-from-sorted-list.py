# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return
        temp=head
        # res=set()
        # while temp.next:
        #     res.add(temp.val)
        #     if temp.next.val in res:
        #         temp.next=temp.next.next
        #     else:
        #         temp=temp.next
        # return head
        while temp and temp.next:
            if temp.val==temp.next.val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head
        