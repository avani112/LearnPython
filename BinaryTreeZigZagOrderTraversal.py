class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None
        
        q = [root]
        ans = []
        while q:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if len(ans) % 2 != 0:
                level = level[::-1]
            ans.append(level)
            
        return ans
