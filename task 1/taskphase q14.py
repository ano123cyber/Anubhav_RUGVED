def first_repeating_element(arr):
    first_seen_at = {}
    min_index = len(arr)
    for i in range(len(arr)):
        element = arr[i]
        if element in first_seen_at:
            original_index = first_seen_at[element]
            if original_index < min_index:
                min_index = original_index
        else:
            first_seen_at[element] = i
    if min_index < len(arr):
        return arr[min_index]
    else:
        return -1
user_input = input("Enter numbers separated by spaces: ")
arr = [int(x) for x in user_input.split()]
result = first_repeating_element(arr)
if result != -1:
    print("The first repeating element is:", result)
else:
    print("There are no repeating elements in the array.")
