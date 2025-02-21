fibonacci_cache = {}

def fibonnaci(n):
    if n not in fibonacci_cache:
        if n <= 1:
            fibonacci_cache[n] = n
        else:
            fibonacci_cache[n] = fibonnaci(n-2) + fibonnaci(n-1)

    return fibonacci_cache[n]


for i in range(101):
    print(i, '->', fibonnaci(i))
