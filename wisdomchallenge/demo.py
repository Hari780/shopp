def sort012(arr):
    n = len(arr)
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        current = arr[mid]
        
        if current == 0:
            temp = arr[low]
            arr[low] = arr[mid]
            arr[mid] = temp
            low += 1
            mid += 1
        elif current == 1:
            mid += 1
        else:
            temp = arr[mid]
            arr[mid] = arr[high]
            arr[high] = temp
            high -= 1

    return arr


examples = [
    [0, 1, 2, 1, 0, 2, 1, 0],
    [2, 2, 2, 2],
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [2, 0, 1],
    []
]
for i in range(len(examples)):
    arr = examples[i]
    print("Example", i+1)
    print("Before sorting:", arr)
    sorted_arr = sort012(arr.copy())
    print("After sorting :", sorted_arr)
   print()