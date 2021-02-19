def high_and_low(numbers):
    output = numbers.split()
    result = list(map(int, output))
    return '' + str(max(result)) + ' ' + str(min(result))