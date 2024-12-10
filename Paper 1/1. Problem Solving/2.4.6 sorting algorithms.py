unsorted_list = [16, 78, 70, 88, 76, 62, 91, 92, 4, 79, 51, 73, 86, 25, 67, 52, 26, 81, 2, 54]

def bubble_sort(input_list: list) -> list:
    num_swapped = None
    num_passes = 0
    checks = 0
    while num_swapped != 0:
        num_swapped = 0
        for i in range(len(input_list)-(num_passes+1)):
            checks += 1
            if input_list[i] > input_list[i+1]:
                
                num_swapped += 1
                temp_value = input_list[i+1]
                input_list[i+1] = input_list[i]
                input_list[i] = temp_value
        num_passes += 1

        print(input_list)

    print(f"Number of checks: {checks}")
    print(f"Number of passes: {num_passes}")
    return input_list

def insertion_sort(input_list: list) -> list:
    list_len = len(input_list) # Get the length of the array
      
    if list_len <= 1:
        return # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, list_len): # Iterate over the array starting from the second element
        key = input_list[i] # Store the current element as the key to be inserted in the right position
        next_val = i-1
        while next_val >= 0 and key < input_list[next_val]: # Move elements greater than key one position ahead
            input_list[next_val+1] = input_list[next_val] # Shift elements to the right
            next_val -= 1
        input_list[next_val+1] = key # Insert the key in the correct position
    return input_list

print(bubble_sort(unsorted_list))
# print(insertion_sort(unsorted_list))