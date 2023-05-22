# 📖 About

Fifth Interpreter is a Python-based interpreter for the stack-based language, Fifth.
The interpreter supports a variety of commands and arithmetic operations.

# 🛠️ Setup

The setup guide assumes you're on a Linux, macOS, or Windows with Python 3.7 or higher installed.

## Setup from Downloaded Zip

1. Unzip the downloaded file into a directory of your choice.

2. Navigate into the directory containing the unzipped files.

3. Run the program using Python:

bash
```
python main.py
```

# 🚀 Usage

After running the main.py file, the interpreter will prompt you to enter commands.
Each line of input should represent a single fifth command.
The result of each command is printed to the console.

Here's an example interaction:

bash
```
Enter a command: PUSH 3
3
Enter a command: PUSH 11
11
Enter a command: +
14
Enter a command: DUP
14
Enter a command: PUSH 2
2
Enter a command: *
28
Enter a command: SWAP
14
Enter a command: /
2
Enter a command: +
ERROR
```

# 🎭 Testing
To run the test suite, navigate to the project root folder and run:

bash
```
python test.py
```

If you wish to run only a specific set of tests, specify the relative path.

bash
```
python -m unittest test.TestInterpreter.test_push
```