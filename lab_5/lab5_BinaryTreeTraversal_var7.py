from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value      # хранимые данные
        self.left = None        # левый потомок
        self.right = None       # правый потомок

def preorder(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.value)            # 1. узел
        preorder(root.left, result)         # 2. левое поддерево
        preorder(root.right, result)        # 3. правое поддерево
    return result

def inorder(root, result=None):
    if result is None:
        result = []
    if root:
        inorder(root.left, result)          # 1. левое поддерево
        result.append(root.value)           # 2. узел
        inorder(root.right, result)         # 3. правое поддерево
    return result

def postorder(root, result=None):
    if result is None:
        result = []
    if root:
        postorder(root.left, result)        # 1. левое поддерево
        postorder(root.right, result)       # 2. правое поддерево
        result.append(root.value)           # 3. узел
    return result

def level_order(root):
    result = []
    if root is None:
        return result
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        # добавляем детей в очередь
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def left_view(root):

    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == 0:                # первый узел на уровне
                result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result
def test_all_funcs(name,tree):
    print("Тест дерева:", name)
    print(preorder(tree))
    print(inorder(tree))
    print(postorder(tree))
    print(level_order(tree))
    print(left_view(tree))
if __name__ == "__main__":
    tree_null = None
    tree_manual = TreeNode(1)
    tree_manual.left = TreeNode(2)
    tree_manual.right = TreeNode(3)
    tree_manual.left.left = TreeNode(4)
    tree_manual.left.right = TreeNode(5)
    tree_manual.right.right = TreeNode(6)
    tree_manual.right.right.right = TreeNode(7)
    tree_only_right = TreeNode(10)
    tree_only_right.right = TreeNode(15)
    tree_only_right.right.right = TreeNode(20)
    tree_only_right.right.right.right = TreeNode(25)
    tree_only_right.right.right.right.right = TreeNode(30)
    test_all_funcs("Пустое дерево", tree_null)
    test_all_funcs("Обычное дерево", tree_manual)
    test_all_funcs("Только правая часть дерева", tree_only_right)

