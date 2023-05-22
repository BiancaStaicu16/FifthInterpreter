from interpreter import FifthInterpreter

def main():
    """
    Main function to run the FifthInterpreter.
    
    This function initializes the interpreter and enters into a loop, 
    asking for user input until the user types "Quit".
    For each command entered, it processes the command using the interpreter and prints 
    the resulting stack or an error message.
    """
    interpreter = FifthInterpreter()
    while True:
        try:
            command = input("Enter a command: ")
            if command.lower() == "Quit":
                break
            print(interpreter.process_command(command))
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()