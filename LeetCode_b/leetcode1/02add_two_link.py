class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummyHead = ListNode(0)
        p = l1
        q = l2
        curr = dummyHead
        carry = 0
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            sum = carry + x + y
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if p:
                p = p.next
            if q:
                q = q.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummyHead.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    res = Solution().addTwoNumbers(l1, l2)
    while res:
        print(res.val)
        res = res.next
