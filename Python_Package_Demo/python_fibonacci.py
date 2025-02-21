def fibonnaci(n):
    if n <= 1:
        return n
    else:
        num1 = 0
        num2 = 1
        for i in range(1, n):
            temp = num1 + num2
            num1 = num2
            num2 = temp

        return num2


for i in range(51):
    print(i, '->', fibonnaci(i))
