import unittest
from interpreter import FifthInterpreter

class TestInterpreter(unittest.TestCase):
    def setUp(self):
        self.interpreter = FifthInterpreter()

    def test_push(self):
        output = self.interpreter.process_command("PUSH 5")
        self.assertEqual(output, "[5]")

    def test_pop(self):
        self.interpreter.process_command("PUSH 5")
        output = self.interpreter.process_command("POP")
        self.assertEqual(output, "[]")

    def test_pop_error(self):
        output = self.interpreter.process_command("POP")
        self.assertEqual(output, "Stack is empty. Cannot perform POP.")

    def test_swap(self):
        self.interpreter.process_command("PUSH 5")
        self.interpreter.process_command("PUSH 3")
        output = self.interpreter.process_command("SWAP")
        self.assertEqual(output, "[3, 5]")

    def test_swap_error(self):
        self.interpreter.process_command("PUSH 5")
        output = self.interpreter.process_command("SWAP")
        self.assertEqual(output, "Not enough elements in stack to perform SWAP.")

    def test_duplicate(self):
        self.interpreter.process_command("PUSH 5")
        output = self.interpreter.process_command("DUP")
        self.assertEqual(output, "[5, 5]")

    def test_duplicate_error(self):
        output = self.interpreter.process_command("DUP")
        self.assertEqual(output, "Stack is empty. Cannot perform DUP.")

    def test_arithmetic_add(self):
        self.interpreter.process_command("PUSH 5")
        self.interpreter.process_command("PUSH 3")
        output = self.interpreter.process_command("+")
        self.assertEqual(output, "[8]")

    def test_arithmetic_subtract(self):
        self.interpreter.process_command("PUSH 5")
        self.interpreter.process_command("PUSH 3")
        output = self.interpreter.process_command("-")
        self.assertEqual(output, "[2]")

    def test_arithmetic_multiply(self):
        self.interpreter.process_command("PUSH 5")
        self.interpreter.process_command("PUSH 3")
        output = self.interpreter.process_command("*")
        self.assertEqual(output, "[15]")

    def test_arithmetic_divide(self):
        self.interpreter.process_command("PUSH 10")
        self.interpreter.process_command("PUSH 2")
        output = self.interpreter.process_command("/")
        self.assertEqual(output, "[5]")

    def test_arithmetic_divide_by_zero(self):
        self.interpreter.process_command("PUSH 10")
        self.interpreter.process_command("PUSH 0")
        output = self.interpreter.process_command("/")
        self.assertEqual(output, "Division by 0 cannot be performed.")

    def test_invalid_command(self):
        output = self.interpreter.process_command("INVALID")
        self.assertEqual(output, "Invalid command: INVALID")

if __name__ == "__main__":
    unittest.main()
