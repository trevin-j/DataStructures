The following code is one of many possible solutions.

You can download this file [here](stacksolution.py).

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
    # Determine the middle
    middle = len(stack) // 2

    # Create another stack to keep half of the stack in
    other_stack = []

    # Iterate through stack, moving the last elements from one stack to another until
    # it can pop and return the middle element.
    for _ in range(middle):
        other_stack.append(stack.pop())

    # Get the middle element and pop it
    value = stack.pop()

    # Move all of the elements from other_stack back into stack
    for _ in range(len(other_stack)):
        stack.append(other_stack.pop())

    # Return the value
    return value


# Test the function
my_stack = [0, 1, 2, 3, 4, 5, 6]

print(pop_middle(my_stack)) # Should print 3
print(my_stack) # Should print [0, 1, 2, 4, 5, 6]

print(pop_middle(my_stack)) # Should print 2
print(my_stack) # Should print [0, 1, 4, 5, 6]
```