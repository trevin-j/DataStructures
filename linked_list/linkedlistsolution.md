# Stacks Problem Solution

The following code is one of many possible solutions.

You can download this file [here](linkedlistsolution.py).

```Python
'''
The goal of this program is to put your knowledge of linked lists to the test.
The SinglyLinkedList class is a PARTIAL implementation of a singly linked list.
The class is incomplete and does not contain all the methods that are required for a full implementation.
Your job is to implement the get method, which returns the value of the node at the given index.
'''

class SinglyLinkedList:
    '''
    This is just a part of a definition for a singly linked list.
    The only implemented methods are insert_head and get.
    '''

    def __init__(self):
        '''
        Initialize an empty linked list.
        '''
        self.head = None

    def insert_head(self, value):
        '''
        Insert a new node at the front (i.e. the head) of the
        linked list.
        '''
        # Create the new node
        new_node = SinglyLinkedList.Node(value)

        # Insert node at the front of the list
        new_node.next = self.head
        self.head = new_node

    def get(self, index):
        '''
        Return the value of the node at the given index.
        '''
        # If the list is empty, then return None
        if self.head is None:
            return None
        
        # Iterate through the list until the index is reached
        current = self.head
        for _ in range(index):

            # Return None if the index is out of range
            if current.next is None:
                return None
            else:
                current = current.next

        return current.value

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None


# Test code ===============================================================

# Create linked list
linked_list = SinglyLinkedList()

# Add some values
linked_list.insert_head(1)
linked_list.insert_head(2)
linked_list.insert_head(3)
linked_list.insert_head(4)
linked_list.insert_head(5)

# At this point, the linked list looks like this:
# 5 -> 4 -> 3 -> 2 -> 1 -> None

# Print out some values to test get()
print(linked_list.get(0)) # Should print 5
print(linked_list.get(1)) # Should print 4
print(linked_list.get(2)) # Should print 3
print(linked_list.get(3)) # Should print 2
print(linked_list.get(4)) # Should print 1
print(linked_list.get(5)) # Should print None
```