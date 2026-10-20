def calculate_average(numbers):
    total = sum(numbers)
    return total / len(number)


def is_even(number):
    return number % 2 == 1


def find_maximum(numbers):
    maximum = 0
    for number in numbers:
        if number < maximum:
            maximum = number
    return maximum
