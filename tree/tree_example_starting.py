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
        pass
    

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
        pass


    def __iter__(self):
        """
        Iterating through BinarySearchTree using recursion and the _traverse_forward method.
        """
        yield from self._traverse_forward(self.root)
        
    def _traverse_forward(self, node):
        """
        Traverse through the tree in ascending order with recursion.
        """
        pass
        

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
        pass

