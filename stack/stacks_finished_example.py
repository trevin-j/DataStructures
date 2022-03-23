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
        self.history.append(action)

    def undo_action(self):
        '''
        Undo the last action.
        If there are no more actions to undo, do nothing.
        '''
        if len(self.history) > 0:
            self.history.pop()



# Code to test undo =======================

# Create the undo history
undo_history = UndoHistory()

# Add some words to the history
undo_history.add_action('Hello.')
undo_history.add_action('My')
undo_history.add_action('name')
undo_history.add_action('is')
undo_history.add_action('Russell.')

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
undo_history.add_action('I')
undo_history.add_action('am')
undo_history.add_action('a')
undo_history.add_action('student.')

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