"""

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


"""

"""递归"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0

        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)

        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)  # isn't leave


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum_ = 0
        if not root:
            return 0

        ans = [root]
        while ans:
            r = ans.pop()
            if r.left and not r.left.left and not r.left.right:
                sum_ += r.left.val
            if r.left:
                ans.append(r.left)
            if r.right:
                ans.append(r.right)
        return sum_
