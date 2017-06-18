needs sort/simple.py stats/average.py
def stats_quartiles(numbers):
    """
    Takes a list of numbers and returns the first, median and third quartiles

    :param numbers: the numbers list
    :return: the first, median and third quartiles
    """
    numbers = sort_simple(numbers)
    first_quartile = 0
    median = 0
    third_quartile = 0
    n = len(numbers)
    if n % 2 == 0:
        first_quartile = stats_average(numbers[0:n // 2])
        median = stats_average(numbers[n // 2:(n // 2 + 1)])
        third_quartile = stats_average(numbers[n // 2:])
    else:
        first_quartile = stats_average(numbers[0:n // 2])
        median = numbers[n // 2]
        third_quartile = stats_average(numbers[(n // 2) + 1:])
    return first_quartile, median, third_quartile
