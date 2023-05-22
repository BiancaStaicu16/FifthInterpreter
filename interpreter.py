from stack import Stack
class FifthInterpreter:
    """Interpreter for the Fifth language."""

    def __init__(self):
        """Initialize the interpreter with an empty stack."""
        self.stack = Stack()

    def process_command(self, command):
        """
        Process a single Fifth command.

        Args:
            command (str): The command to process.

        Returns:
            str: The string representation of the current state of the stack.

        Raises:
            ValueError: If the command is invalid.
        """
        try:
            if command.startswith("PUSH"):
                _, num = command.split()
                self.stack.push(int(num))
            elif command == "POP":
                self.stack.pop()
            elif command == "SWAP":
                self.stack.swap()
            elif command == "DUP":
                self.stack.duplicate()
            elif command in ['+', '-', '*', '/']:
                self.perform_arithmetic(command)
            else:
                raise ValueError(f"Invalid command: {command}")
            return str(self.stack)
        except ValueError as e:
            return str(e)

    def perform_arithmetic(self, operator):
        """
        Perform an arithmetic operation on the top two elements of the stack.

        Args:
            operator (str): The operator to apply. Must be one of ['+', '-', '*', '/'].

        Raises:
            ValueError: If the stack does not have at least two elements or if trying to divide by zero.
        """
        if len(self.stack.stack) >= 2:
            a = self.stack.pop()
            b = self.stack.pop()

            if operator == '+':
                result = b + a
            elif operator == '-':
                result = b - a
            elif operator == '*':
                result = b * a
            else:
                if a != 0:
                    result = b // a
                else:
                    raise ValueError("Division by 0 cannot be performed.")
            self.stack.push(result)
        else:
            raise ValueError("There are not enough elements in stack to perform arithmetic operation.")