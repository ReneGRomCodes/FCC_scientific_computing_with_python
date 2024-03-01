# Learn Tree Traversal by Building a Binary Tree:
# You'll learn how to construct your own BST and perform an in-order traversal. You'll also learn key operations like
# insertion, search, and deletion.


class TreeNode:
    """A class representing a node in a binary tree."""

    def __init__(self, key):
        """Initializes a TreeNode with the given key."""
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        """Returns a string representation of the TreeNode."""
        return str(self.key)


class BinarySearchTree:
    """A class representing a Binary Search Tree (BST)."""

    def __init__(self):
        """Initializes an empty BST."""
        self.root = None

    def insert(self,key):
        """Inserts a key into the BST."""
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        """Recursively inserts a key into the BST and returns updated node."""
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        """Searches for a key in the BST and returns the node containing the key if found, None otherwise."""
        return self._search(self.root, key)

    def _search(self, node, key):
        """Recursively searches for a key in the BST and returns the node containing the key if found, None
        otherwise."""
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        """Deletes a key from the BST."""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        """Recursively deletes a key from the BST and returns the updated node after deletion."""
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)
        return node

    def _min_value(self, node):
        """Finds the minimum value node in a subtree and returns the minimum value in the subtree."""
        while node.left is not None:
            node = node.left
        return node.key

    def inorder_traversal(self):
        """Performs an inorder traversal of the BST and returns a list containing the keys in sorted order."""
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        """Recursively performs an inorder traversal of the BST."""
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)


bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

for node in nodes:
    bst.insert(node)


print("Inorder traversal:", bst.inorder_traversal())
print("Search for 40:", bst.search(40))
bst.delete(40)
print("Inorder traversal after deleting 40:", bst.inorder_traversal())
print("Search for 40:", bst.search(40))
