def slicer(tuple, element):
    if element in tuple:
        if tuple.count(element) > 1:
            first_ind = tuple.index(element)
            second_ind = tuple.index(element, first_ind + 1) + 1
            return tuple[first_ind:second_ind]
        else:
            return tuple[tuple.index(element):]
    else:
        return ()


print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 4))