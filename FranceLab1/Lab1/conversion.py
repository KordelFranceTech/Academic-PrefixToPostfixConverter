#conversion.py
#Kordel France
########################################################################################################################
#This file performs all operations in converting mathematical prefix expressions to postfix expressions.
########################################################################################################################

from Lab1.CharStack import CharStack
from Lab1.StackStack import StackStack
from Lab1.constants import acceptable_chars, acceptable_operators

def prefixToPostfix(stack, stack_length) -> [str, bool]:
    """
    Takes a stack and its specified non-empty element count, stack_length.
    The stack_length is specified because we only want to perform processing on elements that are not empty and
        the stack may technically be initialized as longer than the number of elements it currently contains.
    :param stack: stack of type CharStack containing the prefix expression to be evaluated.
    :param stack_length: integer count of how many non-empty elements exist in stack CharStack.
    :returns [str, bool]: an array containing:
                        1) a string of the evaluated prefix expresssion
                        2) a boolean value indicating whether or not the prefix expression contained invalid characters
    """
    stack_string = get_string_from_stack(stack)
    char_flag = False
    illegal_stack = CharStack(stack_length)
    # CharStack for storing prefix CharStack
    char_stack_a = stack
    # auxiliary CharStack for conversion
    char_stack_b = CharStack(stack_length)
    # StackStack for storing operations, or CharStacks
    stack_stack = StackStack(stack_length)
    operators = set(acceptable_operators)

    # iterating through each character in prefix expression
    for i in range(0, stack_length):
        if char_stack_a.peek() in operators:
            global a
            global b
            global c

            try:
                char_stack_b.peek()
            except IndexError:
                return [f'Too many operators for operands in prefix string: {stack_string}.', True]
            a = char_stack_b.pop()

            try:
                char_stack_b.peek()
            except IndexError:
                return [f'Too many operators for operands in prefix string: {stack_string}.', True]
            b = char_stack_b.pop()

            try:
                char_stack_a.peek()
            except IndexError:
                return [f'Too many operators for operands in prefix string: {stack_string}.', True]
            c = char_stack_a.pop()

            global temp
            if a != None:
                temp = a
            if b != None:
                temp += b
            if c != None:
                temp += c
            if temp != None:
                char_stack_b.push(temp)

            t = CharStack(3)
            t.push(a)
            t.push(b)
            t.push(c)
            stack_stack.push(t)

        # else if operand
        elif char_stack_a.peek() in acceptable_chars:
            char_stack_b.push(char_stack_a.pop())
        else:
            char_flag = True
            illegal_stack.push(char_stack_a.peek())
            char_stack_b.push(char_stack_a.pop())

    # an illegal character was encountered, char_flag was set to true
    if char_flag:
        postfix_str = f'The characters {illegal_stack.items} are illegal in the given prefix string: {stack_string}.\n'\
                      f'Only alphabetical characters and operands of type {operators} are acceptable.'
        return [postfix_str, char_flag]
    # no illegal characters, prefix conversion successful
    else:
        postfix_str = char_stack_b.pop()
        return [postfix_str, char_flag]

def get_string_from_stack(stack):
    string = ''
    for item in stack.items:
        string += str(item)
    return string


