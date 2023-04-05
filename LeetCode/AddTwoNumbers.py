# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    res = ListNode()
    atual = res

    aux = 0
    while l1 or l2 or aux:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        val = v1 + v2 + aux
        aux = val // 10
        val = val % 10
        atual.next = ListNode(val)

        atual = atual.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return res.next