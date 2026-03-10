def read_file_lines(file: str):
    with open(file, 'r', encoding='utf-8') as file: # opens the file in read mode
        data = file.readlines() # read file data
        return data # return file data
    
def total_file_lines(file: str):
    file_data = read_file_lines(file)

    total = 0

    for line in file_data:
        line = int(line)
        total += line
    return total

def append_file_data(file: str, text: str):
    with open(file, 'a', encoding='utf-8') as file:
        file.write(text)

print(total_file_lines("test_file.txt"))