def bubble_sort(arr1):
    a=len(arr1)
    for i in range(a):
        swapped = False
        for j in range(0,a-i-1):
            if arr1[j] > arr1[j+1]:
                arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
                swapped = True
        if not swapped:
            break

# arr1 = [5,4,3,2,1]
# print(arr1)
# bubble_sort(arr1)
# print(arr1)

print(15//3)