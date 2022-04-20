# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        if(head==None and head.next==None):
            return head
        curr=head
        prev=None
        fast=head.next
        while(fast!=None):
            curr.next=prev
            prev=curr
            curr=fast
            fast=fast.next
        curr.next=prev
        return curr
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head==None or  head.next==None:
            return 
        slow=head
        fast=head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        fast=self.reverse(slow.next)
        slow.next=None
        slow=head
        temp=None
        while(fast!=None):
            temp=slow.next
            slow.next=fast
            fast=fast.next
            slow.next.next=temp
            slow=temp

        
        