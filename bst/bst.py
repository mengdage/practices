import random
from collections import deque

class TreeNode:
    def __init__(self, key, val, left = None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.size = 1

    def __str__(self):
        return '<{key}, {val}>'.format(key = self.key, val = self.val)

    def __repr__(self):
        return '<{key}, {val}>'.format(key = self.key, val = self.val)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def put(self, key, val):
        self.root = self.put_helper(self.root, key, val)

    def put_helper(self, node, key, val):
        if not node:
            return TreeNode(key, val)

        if key < node.key:
            node.left = self.put_helper(node.left, key, val)
        elif key > node.key:
            node.right = self.put_helper(node.right, key, val)
        else:
            node.val = val

        node.size = 1 + self._size_helper(node.left) + self._size_helper(node.right)

        return node
    
    def get(self, key):
        node = self.root

        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node

        return None

    def min(self):
        p = self.root
        if not p:
            return None
        
        while p.left:
            p = p.left
        
        return p

    def max(self):
        p = self.root
        if not p:
            return None
        
        while p.right:
            p = p.right
        
        return p
    
    def max_sum_sub_tree(self):
        _, max_sub_tree, _ = self._max_sum_sub_tree_helper(self.root)
        return max_sub_tree

    def _max_sum_sub_tree_helper(self, root):
        # max of mst_left, mst_right, root.val + sum_left + sum_right

        # edge case None
        if root is None:
            return float('-inf'), None, 0

        max_sum_left, max_sub_tree_left, sum_left = self._max_sum_sub_tree_helper(root.left)
        max_sum_right, max_sub_tree_right, sum_right = self._max_sum_sub_tree_helper(root.right)

        sum_root = root.val + sum_left + sum_right

        max_sum = float('-inf')
        max_sub_tree = None

        cands = [(max_sum_left, max_sub_tree_left), (max_sum_right, max_sub_tree_right), (sum_root, root) ]
        for max_sum_cand, max_sub_tree_cand in cands:
            if max_sum_cand > max_sum:
                max_sum = max_sum_cand
                max_sub_tree = max_sub_tree_cand

        return max_sum, max_sub_tree, sum_root

    def rank(self, key):
        return self._rank_helper(self.root, key)

    def _rank_helper(self, node, key):
        if not node:
            return 0

        if key < node.key:
            return self._rank_helper(node.left, key)
        elif key > node.key:
            return self._size_helper(node.left) + 1 + self._rank_helper(node.right, key)
        else:
            return self._size_helper(node.left) + 1

    def floor(self, key):
        return self._floor_helper(self.root, key)

    def _floor_helper(self, node, key):
        if node is None:
            return None

        if key < node.key:
            # the floor must be in the left sub tree
            return self._floor_helper(node.left, key)
        elif key > node.key:
            # the floor might be in the right sub tree
            floor_right = self._floor_helper(node.right, key)

            if floor_right is not None:
                return floor_right

            # if a floor does not exist in the right sub tree,
            # the current node is the floor
            return node

    def ceil(self, key):
        return self._ceil_helper(self.root, key)

    def _ceil_helper(self, node, key):
        if node is None:
            return None

        if key > node.key:
            # the ceiling must be in the right sub tree
            return self._ceil_helper(node.right, key)
        elif key < node.key:
            # the ceiling mnight be in the left sub tree
            ceil_left = self._ceil_helper(node.left, key)

            if ceil_left is not None:
                return ceil_left

            # if a ceil does not exist in the left sub tree,
            # the current node is the ceil  
            return node


    def size(self):
        return self._size_helper(self.root)

    def _size_helper(self, node):
        if not node:
            return 0
        return node.size

    def inorder(self):
        results = []
        stack = []
        node = self.root

        while node:
            stack.append(node)
            node = node.left
        
        while stack:
            cur = stack.pop()
            results.append(cur)

            p = cur.right
            while p:
                stack.append(p)
                p = p.left

        return results

    def __str__(self):
        queue = deque([self.root])
        results = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()

                if node is None:
                    level.append('#')
                    continue

                level.append(node.val)

                queue.append(node.left)
                queue.append(node.right)

            results.append(level)
            
        return str(results)
                




if __name__ == "__main__":
    bst = BinarySearchTree()
    nums = [random.randint(-100, 100) for _ in range(10)]
    for n in nums:
        bst.put(n, n)

    print(bst.get(nums[0]))
    print(bst.inorder())
    print('---- tree structure')
    print(bst)
    print('---- min')
    print(bst.min())
    print('---- max')
    print(bst.max())
    print(bst.size())
    print(bst.rank(nums[0]))
    print(bst.rank(100))

    print('---- ceiling')
    print(bst.ceil(100))
    print(bst.ceil(10))
    print(bst.ceil(0))

    print('---- floor')

    print(bst.floor(100))
    print(bst.floor(10))
    print(bst.floor(0))


    print('---- max sub tree')
    print(bst.max_sum_sub_tree())
