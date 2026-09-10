def first_repeating_element(arr):
    seen = set()
    first_repeating = -1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] in seen:
            first_repeating = arr[i]
        else:
            seen.add(arr[i])
    return first_repeating
user_input = input("Enter numbers separated by spaces: ")
arr = [int(x) for x in user_input.split()]
result = first_repeating_element(arr)
if result != -1:
    print("The first repeating element is:", result)
else:
    print("There are no repeating elements in the array.")