"""
# Definition for a Node.

https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        leftMost = root
        while leftMost.left:
            head = leftMost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next =  head.next.left
                head = head.next
            leftMost = leftMost.left
        return root
      