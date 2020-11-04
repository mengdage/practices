from treeutils.tree import createBT

def inorderRecursion(node):
    if not node:
        return
    
    # 1. visit the left sub tree first
    inorderRecursion(node.left)

    # 2. visit the current node
    print(node)

    # 3. visit the right sub tree last
    inorderRecursion(node.right)

def inorderIteration(node):
    stack = []
    # find the left most node
    while node:
        stack.append(node)
        node = node.left

    while stack:
        # get the sub root
        node = stack.pop()
        print(node)

        # include sub right tree
        node = node.right
        while node:
            stack.append(node)
            node = node.left

def inorderListRecursion(node):
    if not node:
        return []

    return inorderListRecursion(node.left) + [node] + inorderListRecursion(node.right)

if __name__ == '__main__':
    root = createBT([5, 3, 8, 2, 4, 6, 10, 1, '#', '#', '#', '#', '#', '#', 11])
    inorderRecursion(root)
    inorderIteration(root)
    print(inorderListRecursion(root))