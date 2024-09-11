def array_function(param):
    odd_count = 0
    even_count = 0
    for number in param:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return [odd_count, even_count]