def max_value(numbers):
    max_value = 0
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
