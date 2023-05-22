class Stack:
    """Stack implementation for the Fifth interpreter."""

    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []

    def push(self, x):
        """Push an integer onto the stack."""
        self.stack.append(x)

    def pop(self):
        """
        Pop the top element from the stack.

        Raises:
            ValueError: If the stack is empty.
        """
        if not self.is_empty():
            return self.stack.pop()
        raise ValueError("Stack is empty. Cannot perform POP.")

    def swap(self):
        """
        Swap the top two elements of the stack.

        Raises:
            ValueError: If the stack does not have at least two elements.
        """
        if len(self.stack) >= 2:
            self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
        else:
            raise ValueError("Not enough elements in stack to perform SWAP.")

    def duplicate(self):
        """
        Duplicate the top element of the stack.

        Raises:
            ValueError: If the stack is empty.
        """
        if not self.is_empty():
            self.stack.append(self.stack[-1])
        else:
            raise ValueError("Stack is empty. Cannot perform DUP.")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def __str__(self):
        """Return string representation of the stack."""
        return str(self.stack)