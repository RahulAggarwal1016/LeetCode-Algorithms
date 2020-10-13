# Binary Search

def binarySearch(target, array):
    """
    Input:
    Param -- Takes in two arguements, an integer (target) and a list (array)
    Output:
    Return -- A singular integer type value (middle)
    Purpose:
    To find the index location of "target" in "array"
    """

    left = 0
    right = len(array) - 1

    while left < right:
        middle = (left + right)//2
        if array[middle] < target:
            left = middle + 1
        elif array[middle] > target:
            right = middle - 1
        else:
            return middle
