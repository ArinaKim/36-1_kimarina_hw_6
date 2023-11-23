def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def binary_search(element, arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1

unsorted_list = [64, 34, 25, 12, 22, 11, 90]

sorted_list_bubble = bubble_sort(unsorted_list)
print("Sorted list (bubble sort):", sorted_list_bubble)

sorted_list_selection = selection_sort(unsorted_list)
print("Sorted list (selection sort)::", sorted_list_selection)

element_to_search = 25
index = binary_search(element_to_search, sorted_list_bubble)
if index != -1:
    print(f"Element {element_to_search} found at position {index}")
else:
    print(f"Element {element_to_search} do not found at position")
