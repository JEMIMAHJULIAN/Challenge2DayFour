def recur_sum(numbers):
    
    total = 0

    for index in range(len(numbers)):
        if isinstance(numbers[index], list):
            return total + recur_sum(numbers[index])

        total += numbers[index]
        return total
