import Interpreter


if __name__ == "__main__":
    while True:
        text = input("What would you like to do?\n")
        response = Interpreter.respond(text)
