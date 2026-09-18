class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res, stack = [], []
        curr = root
        
        while curr or stack:
            # Reach the leftmost node of the current node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Current must be None at this point
            curr = stack.pop()
            res.append(curr.val)
            
            # We have visited the node and its left subtree; now visit right subtree
            curr = curr.right
            
        return res