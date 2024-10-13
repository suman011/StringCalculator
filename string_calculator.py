def add(numbers):
    if numbers == "":
        return 0

    delimiter = ","

    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = parts[0][2:]
        numbers = parts[1]
    
    numbers = numbers.replace("\n", delimiter)
    
    nums = numbers.split(delimiter)
    
    int_nums = []
    negatives = []
    
    for num in nums:
        if num: 
            n = int(num)
            if n < 0:
                negatives.append(n)
            int_nums.append(n)
    
    if negatives:
        raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negatives))}")
    
    return sum(int_nums)
