def add(numbers):
    if numbers == "":
        return 0
    elif numbers.isnumeric():
        return int(numbers)
    else:
        nums = map(int, numbers.split(","))
        return sum(nums)