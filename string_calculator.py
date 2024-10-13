def add(numbers):
    if numbers == "":
        return 0
    else:
        delimiter = ","
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = parts[0][2:]
            numbers = parts[1]
        numbers = numbers.replace("\n", delimiter)
        nums = map(int, numbers.split(delimiter))
        return sum(nums)