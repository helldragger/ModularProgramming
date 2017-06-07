def stats_average(numbers):
    """
    Returns the average of a serie of values
    :param numbers: the numbers of the serie
    :return: the average of the serie
    """
    n = len(numbers)
    total = 0
    for value in numbers:
        total += value
    return total / n
