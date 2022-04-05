class BinarySearchTree:
    """
    Binary Tree implementation with recrusion.
    """

    class Node:
        """
        A node in the binary tree.
        """

        def __init__(self, data):
            """
            Instantiate a node with data and empty child nodes.
            """
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Instantiate a binary tree with no data.
        """
        self.root = None

    def insert(self, data):
        """
        Insert data into the tree.
        """
        if self.root is None:

            # Add a root node if the tree is empty.
            self.root = BinarySearchTree.Node(data)
        else:

            # Recursively find the right place to insert the data.
            self._insert(data, self.root)

    
    def _insert(self, data, node):
        """
        Recursively find a place to insert the data.
        """
        if data < node.data:

            # If the data will go to the left
            if node.left is None:
                node.left = BinarySearchTree.Node(data)

            else:
                self._insert(data, node.left)
        elif data > node.data:

            # If the data will go to the right
            if node.right is None:
                node.right = BinarySearchTree.Node(data)

            else:
                self._insert(data, node.right)
    

    def __contains__(self, data):
        """ 
        Check if data is stored in the tree.
        """
        # Call the recursive contains method.
        return self._contains(data, self.root)

    
    def _contains(self, data, node):
        """
        Recursively search for data in the tree.
        """
        if node is None:

            # If it found where the data should be and it is None, return False.
            return False

        elif data == node.data:

            # If the data is found, return True.
            return True

        elif data < node.data:

            # If the data is smaller than the current node, search the left subtree.
            return self._contains(data, node.left)

        else:

            # If the data is bigger than the current node, search the right subtree.
            return self._contains(data, node.right)


    def __iter__(self):
        """
        Iterating through BinarySearchTree using recursion and the _traverse_forward method.
        """
        yield from self._traverse_forward(self.root)
        
    def _traverse_forward(self, node):
        """
        Traverse through the tree in ascending order with recursion.
        """
        if node is not None:

            # First traverse the left subtree.
            yield from self._traverse_forward(node.left)

            # Then yield the current node.
            yield node.data

            # Then traverse the right subtree.
            yield from self._traverse_forward(node.right)
        

    def get_height(self):
        """
        Get the height of the tree.
        """
        if self.root is None:
            return 0

        else:
            # Recursively get the height of the tree.
            return self._get_height(self.root)


    def _get_height(self, node):
        """
        Recursively get the height of the tree.
        """
        if node is not None:

            # Get the height of the left subtree.
            len_left = self._get_height(node.left)

            # Get the height of the right subtree.
            len_right = self._get_height(node.right)
            
            # Return the bigger one plus one.
            return 1 + max(len_left, len_right)
        else:
            return 0


    def __reversed__(self):
        """
        Iterating through BinarySearchTree using recursion and the _traverse_backward method.
        """
        yield from self._traverse_backward(self.root)

    def _traverse_backward(self, node):
        """
        Traverse through the tree in descending order with recursion.
        """
        if node is not None:

            # First traverse the right subtree.
            yield from self._traverse_backward(node.right)

            # Then yield the current node.
            yield node.data

            # Then traverse the left subtree.
            yield from self._traverse_backward(node.left)


if __name__ == "__main__":
    # Some test code to see if _traverse_backward works.
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    tree.insert(1)
    tree.insert(9)
    
    # Print the tree in ascending order.
    print("Ascending order:")
    for i in tree:
        print(i)    # Prints 1, 2, 3, 4, 5, 6, 7, 8, 9

    # Print the tree in descending order.
    print("Descending order:")
    for i in reversed(tree):
        print(i)    # Prints 9, 8, 7, 6, 5, 4, 3, 2, 1

