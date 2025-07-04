def add(numbers) :
    if numbers == "" :
        return 0
    # "//;\n1;2;"
    delimiter = ","
    if numbers.startswith("//") :
        delimiter = numbers[2]
        numbers = numbers[4:]
    numbers = numbers.replace("\n",delimiter)
    nums = list(int(x) for x in numbers.split(delimiter) if x)

    negatives = [num for num in nums if num < 0 ]
    if negatives :
        raise Exception("negative numbers not allowed " + ",".join(map(str,negatives)))
    
    return sum(nums)