# inserton sort
array = [1, 3, 55, 7, 5, 4, 3, 23, 33, 43, 0, 3]
a = len(array)


def insertion_sort():
    global a
    global array
    for x in range(1, a):
        currentvalue = array[x]
        position = x - 1
        while position >= 0 and currentvalue < array[position]:
            array[position + 1] = array[position]
            position = position - 1
        array[position + 1] = currentvalue
    print("Your sorted array", array)


insertion_sort()
