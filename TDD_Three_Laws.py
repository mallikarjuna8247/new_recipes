import re

def add(numbers):
    if numbers =="":
        return 0

    delimiters = [',','\n']

    if numbers.startswith('//'):
        delimiter,numbers = numbers[2:].split('\n',1)
        delimiters.append(delimiter)

    pattern = '|'.join(map(re.escape,delimiters))
    numbers = re.split(pattern,numbers)

    numbers = [int(num) for num in numbers if num and int(num) <= 1000]

    negatives = [num for num in numbers if num <0]
    if negatives:
        raise ValueError(f"negatives not allowed: {', '.join(map(str,negatives))}")
    return sum(numbers)

print(add('//;\n1,2,3,,4'))
print(add('1001,4'))
print(add('-1,2,3,,4'))