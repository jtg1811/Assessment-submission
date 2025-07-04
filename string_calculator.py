def add(numbers) :
    if numbers == "" :
        return 0
    if "," in numbers :
        return sum([int(x) for x in numbers.split(",")])
    return int(numbers)