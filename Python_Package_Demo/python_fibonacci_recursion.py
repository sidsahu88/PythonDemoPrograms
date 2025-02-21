def fibonnaci(n):
    if n <= 1:
        return n
    else:
        return fibonnaci(n-2) + fibonnaci(n-1)


for i in range(51):
    print(i, '->', fibonnaci(i))
