def sort_list(nums):
    i = 0
    j = 0
    k = len(nums) - 1

    while j <= k:
        if nums[j] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif nums[j] == 1:
            j += 1
        else:
            nums[j], nums[k] = nums[k], nums[j]
            k -= 1
    return nums


ex = [
    [0, 1, 2, 1, 0, 2, 1, 0],
    [2, 2, 2, 2],
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [2, 0, 1],
    []
]

for i in range(len(ex)):
    print("Ex", i+1)
    print(ex[i])
    print(sort_list(ex[i].copy()))
    print()
