def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
<<<<<<< HEAD


    maximun = numbers[0]
    for num in numbers:
        if num > maximun:
            maximun = num

    return maximun


=======
<<<<<<< HEAD
    largest_number = 0

    for number in numbers:
        if number > largest_number:
            largest_number = number

    return largest_number
=======
    maximum = numbers[0]
    for max_num in numbers:
        if max_num > maximum:
            maximum = max_num
    return maximum
>>>>>>> e6ac7961de2ff09d2f3b13a83009860cd02f21ab
    
>>>>>>> 4c862d234d4ee50f7b7146653bf90e8705fab24b



if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
