import re
from getpass import getpass

def clear():
    print("\033[H\033[J", end="")
    
def is_bool(text: str) -> bool:
    return True if text in ["True", "False"] else False
    
def teach_bool() -> None:
    print("""In Python, a boolean is a value that is either True or False. Booleans are used for making comparisons

A boolean may look like this:
my_bool = True""")
    input_is_bool = False
    while not input_is_bool:
        input_bool = input("Please input a boolean (True/False). Remember, booleans in Python must start with an uppercase.\nthis_bool = ")
        input_is_bool = is_bool(input_bool)
        if input_is_bool == False:
            clear()
            print("That is not a valid boolean!")
        else:
            print(f"Well done! {input_bool} is a boolean!")
            getpass("Press enter to continue...")
            clear()

def is_int(text) -> bool:
    try:
        if "." in text:
            raise ValueError
        int(text)
        return True
    except ValueError:
        return False

def teach_int() -> None:
    print("""In Python, an integer is a whole number, this can be either positive or negative.

An integer may look like this:
my_int = 37""")
    input_is_int = False
    while not input_is_int:
        input_int = input("Please input an integer (anything containing 0-9)\nthis_int = ")
        input_is_int(is_int(input_int))
        if input_is_int == False:
            clear()
            print("That is not a valid integer!")
        else:
            print(f"Well done! {input_int} is an integer!")
            getpass("Press enter to continue...")
            clear()

def is_float(text) -> bool:
    try:
        float(text)
        return True
    except ValueError:
        return False

def teach_float() -> None:
    print("""In Python, a float is a number that may include values after the decimal point, this can be either positive or negative.

A float may look like this:
my_float = 12.5""")
    input_is_float = False
    while not input_is_float:
        input_float = input("Please input a float (anything containing 0-9)\nthis_float = ")
        input_is_float = is_float(input_float)
        if input_is_float == False:
            clear()
            print("That is not a valid float!")
        else:
            print(f"Well done! {input_float} is a float!")
            getpass("Press enter to continue...")
            clear()

def is_str(text: str) -> bool:
    return True if text.endswith("\"") else False

def teach_str() -> None:
    print("""In Python, a string is a sequence of zero or more characters (A-Z, 0-9, any special character).

A string may look like this:
my_str = "Hello World" """)
    input_is_str = False
    while not input_is_str:
        input_str = input("Please input a string (any character). The opening \" is provided for you\nthis_str = \"")
        input_is_str(is_str(input_str))
        if input_is_str == False:
            clear()
            print("That is not a valid string! Please make sure you have a closing \"")
        else:
            print(f"Well done! \"{input_str} is a string!")
            getpass("Press enter to continue...")
            clear()

if __name__ == "__main__":
    done_bool, done_int, done_float, done_str = False, False, False, False
    finished = False
    print("""This is an introduction to different data types in python!
This will cover the following:
* Boolean
* Integer
* Real (float)
* String""")
    while not finished:
        try:
            if not done_bool:
                print("First you'll learn about booleans!")
                teach_bool()
                done_bool = True
            elif not done_int:
                print("Next, you'll learn about integers!")
                teach_int()
                done_int = True
            elif not done_float:
                print("Then, you'll learn about floats")
                teach_float()
                done_float = True
            elif not done_str:
                print("Finally, you'll learn about strings!")
                teach_str()
                done_str = True
            else:
                if finished != True:
                    print("Well done, you completed the entire course! Hope it helped!")
                    finished = True
                else:
                    exit(0)
        except (KeyboardInterrupt, EOFError):
            print("Stop trying to be smart, that's not valid. I'm not mad I'm just disappointed 😔")