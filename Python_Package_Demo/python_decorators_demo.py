def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with {args} and {kwargs}" )
        result = func(*args, **kwargs)
        print(f"Called function {func.__name__} returned {result}")
        return result
    return wrapper


@logger # Decorator annotation
def average(*args):
    return sum(args) / len(args)

if __name__ == "__main__":
    average(2, 4, 5, 10)