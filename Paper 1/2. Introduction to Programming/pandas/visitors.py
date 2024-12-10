import pandas

dataset = {
    "Days": ["Monday", "Tuesday", "Wednesday", "Thursday"],
    "Visitors": [74, 55, 23, 88]
}

dataset_frame = pandas.DataFrame(dataset)

print(dataset_frame)