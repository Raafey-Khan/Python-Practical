def sum_of_squares(n):
    sum = 0
    for i in range(1, n+ 1):
        sum += i**2
        return sum
result = sum_of_squares(5)  # You can replace 5 with any desired value
print(result)
