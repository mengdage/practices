class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        return f'<Node: {self.val}>'

    def __str__(self):
        return f'<Node: {self.val}>'

def createNode(nums, i):
    if i < len(nums) and nums[i] != '#':
        return Node(nums[i])
    return None

def createBT(nums):
    if not nums:
        return None
    root = Node(nums[0])
    level = [root]
    p = 1
    while p < len(nums):
        nextLevel = []

        for n in level:
            n.left = createNode(nums, p)
            n.right = createNode(nums, p+1)
            if n.left:
                nextLevel.append(n.left)
            if n.right:
                nextLevel.append(n.right)
            
            p += 2
        level = nextLevel
    return root

def inorder(root):
    stack = []
    p = root
    while p:
        stack.append(p)
        p = p.left
    
    results = []
    while stack:
        p = stack.pop()
        results.append(p.val)

        p = p.right
        while p:
            stack.append(p)
            p = p.left
    return results

if __name__ == '__main__':
    bst1 = [5, 3, 8, 2, 4, 6, 10, 1, '#', '#', '#', '#', '#', '#', 11]
    root = createBT(bst1)
    print(root)
    print(inorder(root))

