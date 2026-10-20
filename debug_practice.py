def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)


def is_even(number):
    return number % 2 == 0


def find_maximum(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
