def simple_sort(l):
    """
    Sorts data from the list l in the most naive manner
    :param l: the list of data
    :return: the sorted data
    """
    r = []
    for data in l:
        if len(r) == 0:
            r.append(data)
        else:
            for index, sorted_data in enumerate(r):
                if sorted_data < data:
                    r.insert(index, data)
                    break
    return r
