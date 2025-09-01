def test_fun(numbers, t):
    i = 0
    temp = None
    min_diff = float('inf')

    while i < len(numbers):
        diff = abs(numbers[i] - t)
        if diff < min_diff:
            min_diff = diff
            temp = numbers[i]
        i += 1

    return temp

data = [4, 12, 8, 3]
t_num = 10
print(test_fun(data, t_num))