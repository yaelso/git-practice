def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    maximum = numbers[0]
    for max_num in numbers:
        if max_num > maximum:
            maximum = max_num
    return maximum
    


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
