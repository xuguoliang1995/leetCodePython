# /usr/bin/env python3
# encoding: utf-8\
class ListNode(object):
    def __init__(self, item):
        self.val = item
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        '''
        :param l1:
        :param l2:
        :return:listNode
        '''
        result = ListNode(0)
        cur = result
        carry = 0
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)
            cur.next = ListNode(out)
            cur = cur.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return result.next
