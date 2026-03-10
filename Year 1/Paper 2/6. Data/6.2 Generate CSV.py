import csv

def generate_exponent(exponents: list, data_range: list) -> list:
    data = {}
    try:
        assert len(data_range) == 2
        assert isinstance(data_range[0], int)
        assert isinstance(data_range[0], int)
        for exponent in exponents:
            data_chunk = []
            for num in range(data_range[0], data_range[1]+1):
                data_chunk.append(num**exponent)
            data[exponent] = data_chunk
        return data
    except AssertionError:
        print("The range must be between 2 integers")
        return ""

def generate_multiples(numbers: list, amount: int) -> list:
    data = {}
    for num in numbers:
        data_chunk = []
        for multiplier in range(1, amount+1):
            data_chunk.append(num * multiplier)
        data[num] = data_chunk
    return data

def write_to_csv(filename: str, data: dict) -> None:
    filename = f"{filename}.csv" if not filename.endswith(".csv") else filename

    row_count = len(data)
    column_count = len(data[next(iter(data))])

    csv_data = ""

    for column in range(column_count+1):
        if column == 0:
            csv_data += str(list(data.keys())).strip("[]")
            print(csv_data)
            # for key in data.keys()

    with open(filename, 'a', encoding='utf-8') as file:
        ...

# print(generate_multiples([1, 2, 3], 5))
# print(generate_exponent([2, 3, 4, 5], [1, 10]))
# write_to_csv("Test", generate_multiples([1, 2, 3], 5))
write_to_csv("Test", generate_exponent([2, 3, 4, 5], [1, 10]))