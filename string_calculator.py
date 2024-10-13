def add(numbers):
    if numbers == "":
        return 0
    else:
        nums = map(int, numbers.split(","))
        return sum(nums)