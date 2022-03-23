# Stacks

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

[View possible solution](stacksolution.py)