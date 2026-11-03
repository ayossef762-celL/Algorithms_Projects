def insertion_sort_with_counts(arr):
    comparisons = 0
    shifts = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr, comparisons, shifts

data = [6, 5, 3, 1, 8, 7, 2, 4]
sorted_arr, comps, sfts = insertion_sort_with_counts(data.copy())
print("Sorted Array:", sorted_arr)
print("Comparisons:", comps)
print("Shifts:", sfts)
