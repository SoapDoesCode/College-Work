import pandas

dataset = {
    "cars": ["BMW", "Volvo", "Ford"],
    "Passings": [3, 7, 2]
}

dataset_frame = pandas.DataFrame(dataset)

print(dataset_frame)