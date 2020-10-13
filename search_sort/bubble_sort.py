def bubbleSort(array):
    """
    Input:
    Param -- Takes in one arguement, a list (array)
    Output:
    Return -- Returns a list type value (array)
    Purpose:
    To sort the list "array" from least to greatest
    """

    swapped = True

    while swapped:
        swapped = False
        for i in range(1, len(array)):
            if array[i-1] > array[i]:
                temp = array[i-1]
                array.remove(temp)
                array.insert(i, temp)
                swapped = True

    return array
