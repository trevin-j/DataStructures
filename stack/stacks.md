# Stack Data Structure

## Introduction

The stack data structure adds and removes data based on a **"List In, First Out" (LIFO)** idea. A stack can be represented in Python using a list.

A stack data structured can be thought of just like a stack of papers. Let's say that we have a stack of papers on our desk. Whenever we set a new piece of paper on that stack, it is called a **push** operation. That paper gets added to the back of the stack, which in this case is on top. If we want to remove a  paper from the stack, we can't easily remove it from the middle, but we can take it right off the top. This is called a **pop** operation. Whenever we do this, we get the top paper and it is removed from the back of the stack. This is why the stack is a last in, first out data structure.

Last in, first out is a great structure to help us remember what has happened. A common usage of a stack is for function calls. You can see this whenever an exception is thrown inside Python code. The console will log the function stack trace. With every new function call, the function is pushed onto the stack unitil it finishes and is popped. The current running function is always the one at the back of the stack.

## Using stacks in Python

To use a stack in Python, we will use a Python list. We use the `append` function to push to the stack. We can use the `pop` function to pop from the stack. The `pop` function removes and returns the object at the back of the stack, or in this case, Python list. We can determine the size of the stack by using the `len` function.

## Performance

The following table shows the performance of stack operations:

| Operation | Python Code | Performance |
|-----------|-------------|-------------|
| push(value) | `stack.append(value)` | O(1) |
| pop(value) | `stack.pop()` | O(1) |
| size() | `len(stack)` | O(1) |
| empty() | `len(stack) == 0` | O(1) |

A stack is a very performant data structure, with a performance of O(1) for these common functions. It is the same performance as adding and removing to the back of, and checking the length of a dynamic array.

## Example

Let's walk through an example problem and how we can use stacks to come to a solution.

### The Problem

A common use for stacks is undo. Stacks make this possible because of their nature to remember what has happened. For this example problem, we will work through and implement our own simple undo system.

Let us start with the following code:

(You can download the starting code file [here](stacks_starting_example.py).)

```Python
'''
The goal of this program is to use a stack to allow a user to undo words that they have typed.
A standard Python list will be used as a stack in this example.
'''

class UndoHistory:
    def __init__(self):
        '''
        Construct the class.
        Create an empty history.
        '''
        self.history = []

    def get_passage(self) -> str:
        '''
        This method will return a string of what the user has typed.
        '''
        return ' '.join(self.history)

    def add_action(self, action: str):
        '''
        This method takes in an action, and puts it in the undo history,
        so it can be undone if necessary.
        '''
        pass

    def undo_action(self):
        '''
        Undo the last action.
        If there are no more actions to undo, do nothing.
        '''
        pass
```

We start with a simple class definition. If we were to use the UndoHistory class right now, it wouldn't work. We need to implement a few methods ourselves first.

### The Solution

Let's start by implementing the `add_action` method. We can see in the `__init__` method that we have already created a stack to hold the undo history. We called this stack `self.history`.

To implement the `add_action` method, we know we will need to do a **push** operation. We learned that in Python, we can use the `list.append` method to do this. 

```Python
def add_action(self, action: str):
        '''
        This method takes in an action, and puts it in the undo history,
        so it can be undone if necessary.
        '''
        self.history.append(action)
```

Great! We now have a way to **push** to the undo history. With every action that the user takes, we can call add_action, and it will remember what the user has done.

But we don't yet have a way to undo any actions! So let's implement the `undo_action` method by using a **pop** operation on the `history` stack. We should now have the following:

```Python
def undo_action(self):
        '''
        Undo the last action.
        If there are no more actions to undo, do nothing.
        '''
        self.history.pop()
```

Awesome! Now we have built a simple undo system. Let's run some test code to test out our class! Paste the following into your file: 

(if you downloaded the file, you should already have this code)

```Python
# Code to test undo =======================

# Create the undo history
undo_history = UndoHistory()

# Add some words to the history
undo_history.add_action('Hello. ')
undo_history.add_action('My ')
undo_history.add_action('name ')
undo_history.add_action('is ')
undo_history.add_action('Russell. ')

# Print the history
print(undo_history.get_passage())

# Now let's say we want to say something else
# Undo some actions
undo_history.undo_action()
undo_history.undo_action()
undo_history.undo_action()
undo_history.undo_action()

# Print the history to show that we have undone some actions
print(undo_history.get_passage())

# Add some new actions
undo_history.add_action('I ')
undo_history.add_action('am ')
undo_history.add_action('a ')
undo_history.add_action('student. ')

# Print the history to show that we have added some new actions
print(undo_history.get_passage())

# Now undo all actions, plus some more to make sure that we don't get an error.
undo_history.undo_action()
undo_history.undo_action()
undo_history.undo_action()
undo_history.undo_action()
undo_history.undo_action()

# This should do nothing, since there are no more actions to undo.
undo_history.undo_action()

# Print the history to show that we have undone all actions
print(undo_history.get_passage())
```

Uh oh! It looks like our program was working... until it didn't. We ran into an IndexError! To fix this, we want to check if there is anything in the history before we undo. This is a simple fix! We want to check the size of the stack to make sure it isn't empty. We can do this with the `len` function in Python.

```Python
def undo_action(self):
        '''
        Undo the last action.
        If there are no more actions to undo, do nothing.
        '''
        if len(self.history) > 0:
            self.history.pop()
```

Great job, our program now runs smoothly! If you want some added challenge, try creating a `redo_action` method for redoing something you have undone! Hint: you'll want to create another stack for this, and you will want to know if another action is added, because you wouldn't want to redo something that happened long before you added another action!

You can download the full solution [here](stacks_finished_example.py).

## Problem

To further your understanding of how stack data structures work, try the following problem.

Start with the following code:

```Python
def pop_middle(stack):
    '''
    This function pops the middle element from a stack, and returns it.
    There are more than one solution to this problem,
    but do not use any data structure other than stacks.

    constraints:
        2 <= len(stack) <= 100

    Hint: the middle element is at the position len(stack) // 2
    '''
    # Your code here...

# Test the function
my_stack = [0, 1, 2, 3, 4, 5, 6]

print(pop_middle(my_stack)) # Should print 3
print(my_stack) # Should print [0, 1, 2, 4, 5, 6]

print(pop_middle(my_stack)) # Should print 2
print(my_stack) # Should print [0, 1, 4, 5, 6]
```

Implement the `pop_middle` function so that it follows all of the directions specified in the function docstring.

[View possible solution](stacksolution.md)