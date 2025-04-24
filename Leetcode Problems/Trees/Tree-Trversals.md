# 🔁 Tree Traversals

## 📚 Recursive vs Iterative

### 🤖 Recursive
- Simple, clean, intuitive for tree problems.
- Risk of stack overflow in deep trees.
- Uses function call stack.

### ⚙️ Iterative
- Manual stack/queue control.
- Safer for deep trees.
- More control over the flow.

| Approach     | Time       | Space (Balanced) | Space (Skewed) |
|--------------|------------|------------------|----------------|
| Recursive    | O(n)       | O(log n)         | O(n)           |
| Iterative    | O(n)       | O(log n)         | O(n)           |
| Level Order  | O(n)       | O(n)             | O(n)           |

---

## 🌿 Inorder (Left → Node → Right)

### ✅ Recursive
```python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
```

### 🔁 Iterative
```python
def inorder_iter(root):
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        print(curr.val)
        curr = curr.right
```

---

## 🌿 Preorder (Node → Left → Right)

### ✅ Recursive
```python
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
```

### 🔁 Iterative
```python
def preorder_iter(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
```

---

## 🌿 Postorder (Left → Right → Node)

### ✅ Recursive
```python
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
```

### 🔁 Iterative (2 stacks)
```python
def postorder_iter(root):
    if not root:
        return
    stack1 = [root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        print(stack2.pop().val)
```

---

## 🌿 Level Order (BFS)

### 🔁 Iterative (Queue)
```python
from collections import deque

def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

### ✅ Recursive (less common)
```python
def level_order_recursive(root):
    levels = []
    def dfs(node, level):
        if not node:
            return
        if level == len(levels):
            levels.append([])
        levels[level].append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    for level in levels:
        print(level)
```

---

## When to use recursive vs iterative traversal
### 🤖 Recursive
Best when:
    1. Problem is naturally divide-and-conquer (e.g., tree traversals, LCA, depth-based problems)
    2. Stack space is not a concern (tree height is small)
    3. Code clarity and simplicity matter more than performance

Downside:
    1. Risk of stack overflow in deep trees (depth > 10^5)
    2. Less control over traversal flow (esp. in customized orders)

### ⚙️ Iterative
Best when:
    1. Tree is very deep (avoids recursion stack overflow)
    2. You need fine-grained control (e.g., simulate traversal, modify order)
    3. Language/platform has low recursion limit (e.g., Java, competitive coding)

Downside:
    1. More boilerplate (managing your own stack)
    2. Code can be less readable

## 📊 Visual Tools
- Use [Visualgo](https://visualgo.net/en) for step-by-step tree traversal animations
- [BST Visualizer](https://www.cs.usfca.edu/~galles/visualization/BST.html) to play with trees and their traversal orders
