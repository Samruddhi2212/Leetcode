# LeetCode usually already provides this definition:
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
        if n == 0:
            return []

        def build(start, end):
            if start > end:
                return [None]  # empty tree placeholder

            all_trees = []
            for i in range(start, end + 1):
                # all possible left and right subtrees
                left_subtrees = build(start, i - 1)
                right_subtrees = build(i + 1, end)

                # combine every left with every right
                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)

            return all_trees

        return build(1, n)