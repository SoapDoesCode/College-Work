file_path = "./names.txt"

class DataAlreadyExists(Exception):
    pass

class NoNamesFound(Exception):
    pass

def write_names(*names):
    formatted_names = "\n".join(names)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_names)

def read_names():
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
        new_data = []
        for name in data:
            new_data.append(name.removesuffix("\n"))
    return new_data

def append_names(*names):
    new_data = []
    for name in names:
        if name.isalpha():
            new_data.append(name)
    if len(new_data) == 0:
        raise NoNamesFound
    new_data[0] = f"\n{new_data[0]}"
    formatted_names = "\n".join(new_data)
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(formatted_names)

write_names("Soap", "Silly") # sets default names in the file

print(f"The file currently contains:\n{read_names()}")

while True:
    try:
        names_to_add = input("What names would you like to add to the file? Separate them by commas!\nNames: ")
        names = names_to_add.split(", ")

        namelist = read_names()
        for name in names:
            if name in namelist:
                raise DataAlreadyExists

        append_names(*names)
        print(f"Here is the updated file data!\n{read_names()}")
    except KeyboardInterrupt:
        print("Worth a shot!")
    except EOFError:
        print("Nice try Alex!")
    except DataAlreadyExists:
        print("You must not enter names that are already in the file!")
    except NoNamesFound:
        print("There were no valid names found")