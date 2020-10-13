# Selection Sort

def selectionSort(array, new_array=[]):
    """
    Input:
    Param -- Takes in one arguement, a list (array)
    Output:
    Return -- A list type value (new_array)
    Purpose:
    To sort the list "array" from least to greatest
    """

    while len(array) != 0:
        minimum = min(array)
        new_array.append(minimum)
        array.remove(minimum)

    return new_array
