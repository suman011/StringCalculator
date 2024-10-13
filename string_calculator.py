def add(numbers):
    if numbers == "":
        return 0
    elif numbers.isnumeric():
        return int(numbers)