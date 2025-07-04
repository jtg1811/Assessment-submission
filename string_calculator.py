def add(numbers) :
    if numbers == "" :
        return 0
    numbers = numbers.replace("\n", ",")
    return sum([int(x) for x in numbers.split(",")])