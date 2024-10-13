def add(numbers):
    if numbers == "":
        return 0
    else:
        numbers = numbers.replace("\n", ",")
        nums = map(int, numbers.split(","))
        return sum(nums)