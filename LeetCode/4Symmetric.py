# -*- coding:UTF-8 -*-

'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    # 判断两颗子树是否对称
    # ==> 判断当前两个节点是否相等, 判断其对应的子树是否对称
    def helper(self, p, q):
        if p is None and q is None:
            return True

        if p and q and p.val == q.val:
            if self.helper(p.left, q.right) and self.helper(p.right, q.left):
                return True

        return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.helper(root.left, root.right)
        return True



if __name__ == '__main__':

    a = TreeNode(1)
    b = TreeNode(2)
    print(Solution().isSameTree(a, b))

