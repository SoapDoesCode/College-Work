# region, property_type, bedrooms, price = None, None, None, None

# while all()

property = [None, None, None, None]

total = 0
while not all(property):
    property[total] = str(total)
    print(property[total])
    total += 1

# print(all(property))