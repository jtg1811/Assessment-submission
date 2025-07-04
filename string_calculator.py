def add(numbers) :
    if numbers == "" :
        return 0
    # "//;\n1;2;"
    delimiter = ","
    if numbers.startswith("//") :
        delimiter = numbers[2]
        numbers = numbers[4:]
    numbers = numbers.replace("\n",delimiter)

    return sum([int(x) for x in numbers.split(delimiter) if x])