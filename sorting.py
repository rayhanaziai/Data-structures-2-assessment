#Sorting


def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    for j in xrange(len(lst)-1):
        i = 0
        swap = False
        while i < len(lst)-1:
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
            i += 1
            swap = True
        if swap is False:
            break
    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """
    result_list = []
    while list1 and list2:
        if list1[0] > list2[0]:
            result_list.append(list2[0])
            list2.pop(0)
        elif list1[0] < list2[0]:
            result_list.append(list1[0])
            list1.pop(0)
    while list1 or list2:
        if not list1 and list2:
            result_list.append(list2[0])
            list2.pop(0)
        if not list2 and list1:
            result_list.append(list1[0])
            list1.pop(0)
    return result_list


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """

    if len(lst) == 1:
        return lst

    midway = int(len(lst)/2)
    lst1 = merge_sort(lst[:midway])
    lst2 = merge_sort(lst[midway:])

    sorted_list = []

    while lst2 and lst1:
        if lst2[0] < lst1[0]:
            sorted_list.append(lst2.pop(0))

        elif lst1[0] < lst2[0]:
            sorted_list.append(lst1.pop(0))

    while lst2:
        sorted_list.append(lst2.pop(0))

    while lst1:
        sorted_list.append(lst1.pop(0))

    return sorted_list


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
