#StackStack.py
#Kordel France
########################################################################################################################
#This file contains the specification class for a stack of CharStacks, which are stacks of single-character strings.
########################################################################################################################

from Lab1.CharStack import CharStack

class StackStack:
    def __init__(self, max_length: int):
        """
        The StackStack class is used to hold stacks of CharStacks in a conventional stack ADT.
        Each element is a CharStack.
        A StackStack is essentially a 'stack of stacks.'
        :param max_length: The maximum number of items allowed to be contained in the stack.
        """
        self.max_items = max_length
        self.items = []

    def is_empty(self) -> bool:
        """
        Used to determine if the stack is holding any elements.
        :return: True if the stack does not currently contain any elements, False otherwise.
        """
        return len(self.items) > 0

    def is_full(self) -> bool:
        """
        Used to determine if the stack contains its maximum number of elements as specified by max_length.
        :return: True if the stack is full, False otherwise.
        """
        return len(self.items) >= self.max_items

    def pop(self) -> CharStack:
        """
        Used to remove one CharStack from the top of the StackStack and returns its value.
        :return: The current CharStack on the top of the StackStack just removed.
        """
        return self.items.pop()

    def peek(self) -> CharStack:
        """
        Used to view the top-most CharStack element of the StackStack and returns its value.
        :return: The current CharStack on the top of the StackStack.
        """
        return self.items[len(self.items) - 1]

    def push(self, charStack: CharStack) -> None:
        """
        Used to push a new CharStack element to the top of the StackStack.
        :param charStack: the CharStack to insert. NOTE: Must be of type CharStack
        """
        if self.max_items <= len(self.items):
            raise OverflowError("Stack exceeds max height")
        elif type(charStack) is not CharStack:
            raise AssertionError(f"This stack only contains CharStacks."
                                 f"Do not insert with type {type(charStack)} into the StackStack")
        self.items.append(charStack)

    def pop_all(self) -> None:
        """
        Used to pop all char elements from the stack and return an empty stack.
        ;return: an empty stack with no elements but the same max_length.
        """
        self.items = []


