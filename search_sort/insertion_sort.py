# Insertion Sort

def insertionSort(array):
    """
    Input:
    Param -- Takes in one arguement, a list (array)
    Output:
    Return -- A singular list type value (array)
    Purpose:
    To sort the list "array" from least to greatest
    """

    i = 1
    while i < len(array):
        j = i
        while j > 0 and array[j-1] > array[j]:
            temp = array[j-1]
            array.remove(temp)
            array.insert(j, temp)
            j -= 1
        i += 1

    return array
