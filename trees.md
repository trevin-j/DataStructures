# Tree Data Structure

## This tutorial is not yet complete.

## Introduction

A tree works similarly to a linked list. When we worked with linked lists, each node pointed to the node before, and the node after. Instead of pointing to the next and previous nodes, the nodes in a tree point to children nodes. One example of a tree would be a family tree, where it starts with one set of parents which have children who grow and have their own children. As you go further down the tree, there are more and more parents.

### Terminology

* Node - A part of the tree which holds the data, as well as a pointer to child nodes.
* Root node - The single node at the top of the tree which has no parent.
* Parent node - The node pointing to a given node.
* Child node - A node that a parent node points to.
* Leaf node - A node which has no child nodes.
* Subtree - A part of the tree formed by a parent node and children nodes.

### Binary tree

One more specific and useful version of a tree is a Binary tree. A binary tree restricts each node to having at most 2 child nodes.

### Binary search tree

A binary search tree is a type of binary tree that is sorted when inserting items. When an item is inserted, recursion is used to find the place where the item should be so that the tree can be sorted. Inserting an item starts with the root node. From there, if the new value is less than the current node, it moves down the tree to the left. If it is greater than the current node, it moves to the right. Once it gets to a spot with no node, one is created and set to the new value. This results in the tree being sorted.

### Balanced binary search tree.

A balanced binary search tree is a binary search tree that keeps the tree mostly even in height. If one subtree begins to grow to tall, it causes the tree to be less performant. This is when an algorithm determines if the tree is unbalanced and performs a node rotation to balance the tree.

A couple common balanced binary search tress are AVL trees and red black trees.

## Using trees in Python

Python does not have any built-in classes to represent trees, but there are libraries that can be used to represent them. For the purposes of this tutorial, we will use our own defined unbalanced binary search tree.

## Performance

| Operation           | Description | Performance |
|---------------------|--------------------------|-------------|
| insert(value)       | Insert a value into the tree | O(log n)        |
| remove(value)       | Remove a value from the tree | O(log n)        |
| contains(value)     | Determine if a value is in the tree | O(log n)        |
| traverse_forward    | Go through all objects smallest to largest | O(n)        |
| traverse_reverse    | Go through all objects greatest to smallest | O(n)        |
| height(node)        | Determine the height of the node/tree | O(n)        |
| size()              | Return the tree size | O(1)        |
| empty()             | Return true if empty, or false otherwise | O(1)        |

## Example

For this example problem, we are going to walk through implementing a binary search tree in Python using recursion.

Download the starting code for the example problem [here](tree/tree_example_starting.py).

We are going to use recursion to implement some missing functionality of the `BinarySearchTree` class. We will implement the following methods:

* `_insert(data, node)`
* `_contains(data, node)`
* `_traverse_forward(node)`
* `_get_height(node)`

Let's start with inserting data into the tree. We know that in order to insert an element, we have to use recursion to find where it belongs. If the new value is less than the current node, we look to the left node. If it's greater, then we look to the right. Once we hit an empty node, we create a new node there. The performance of inserting a value is O(log n).

```Python
    def _insert(self, data, node):
        """
        Recursively find a place to insert the data.
        """
        if data < node.data:
            # If the data is less than the current node's data

            if node.left is None:
                # If the left node doesn't exist, this is where it goes! So let's create it.
                node.left = BinarySearchTree.Node(data)

            else:
                # If there is a node to the left, call this function recursively on the left node.
                self._insert(data, node.left)
        elif data > node.data:
            # If the data is greater than the current node's data

            if node.right is None:
                # If the right node is none, create the node and put it there.
                node.right = BinarySearchTree.Node(data)

            else:
                # If it's a node, continue recursion!
                self._insert(data, node.right)
```

Great! Now we have a working insert method to add elements to the tree! Next, let's implement the `_contains` method. This method is the recursive portion of the method that checks if a value exists in the tree. Similarly to inserting, we will go recursively through the tree, following the left nodes where it is less than, and the right nodes where it is greater than. If we run into the exact value, we return true, but if we run into None, we can return false since the value doesn't exist. Checking if an element exists is O(log n) performance.

```Python
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
```

Now we can successfully check if there are values by using the `in` keyword! For the third implementation, let's add the `_traverse_forward` method. This method is used to go through the tree in a for loop. `_traverse_forward` is called and yields the next element in a for loop when iterating. Again, we will use recursion to get every element in order from the tree. The performance here will be O(n) because we will go through every element in the tree.

```Python
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
```

Now that we have implemented the `_traverse_forward` method, we can easily iterate through the elements with a for loop. The last method to implement is `_get_height`. Getting the height is O(n) performance, because we have to check the height of all subtrees and find the max height.

```Python
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
```

Great! Now that we have implemented these methods, let's test out some driver code to see if it works! Paste the following into the file, and run it to see if it works!

```Python
# Test the BinarySearchTree class.
if __name__ == "__main__":

    # Test insert method.
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)

    # Print the tree, testing the _traverse_forward method.
    for node in bst:
        print(node)   # 2 3 4 5 7

    # Test contains method.
    print(5 in bst)  # True
    print(6 in bst)  # False
    print(3 in bst)  # True
    print(2 in bst)  # True
    print(11 in bst)  # False

    # Test get_height method.
    print(bst.get_height())  # 3
```

Great! If everything was implemented correctly, you now should have a working binary search tree! Remember that this tree is **not** balanced! This means that if you insert all the elements in order, the tree can quickly become imbalanced! This means that operations could become a lot slower, since it becomes more like a linked list than a tree! The tree height would grow and have a performance of O(n) instead of O(log n). This is why most modern implementations of binary search trees use balancing algorithms.

## Problem

For the challenge problem, you will continue with the binary search tree that we defined, and implement the `__reversed__` method. Start with the code [here](tree/tree_challenge_starting.py). Use recursion to implement `_traverse_backward` similarly to how we implemented `_traverse_forward`.

[View possible solution](tree/treesolution.md)

[Return to main page](README.md)