# Merge Sort

def combine(left, right):
    """
    Input:
    Param -- Takes in two arguments, two list type values (left and right)
    Output:
    Return -- A list type value (result)
    Purpose:
    To sort combine left and right while sorting the combined list 
    """

    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])

    while left:
        result.append(left[0])
        left.remove(left[0])
    while right:
        result.append(right[0])
        right.remove(right[0])

    return result


def mergeSort(array):
    """
    Input:
    Param -- Takes in a singular list type value (array)
    Output:
    Return -- A list type value (array)
    Purpose:
    To sort array from least to greatest using the combine function recursively
    """

    if len(array) <= 1:
        return array

    left = []
    right = []

    middle = len(array)//2

    left = array[:middle]
    right = array[middle:]

    left = mergeSort(left)
    right = mergeSort(right)

    return combine(left, right)
