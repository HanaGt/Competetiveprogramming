# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i, lists[i]))

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, idx, node = heappop(heap) 
            curr.next = node
            curr = curr.next

            if node.next:
                heappush(heap, (node.next.val, idx, node.next)) 

        return dummy.next
