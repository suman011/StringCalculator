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
        nums = list(map(int, numbers.split(delimiter)))

        negatives = [num for num in nums if num < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negatives))}")
        
        return sum(nums)