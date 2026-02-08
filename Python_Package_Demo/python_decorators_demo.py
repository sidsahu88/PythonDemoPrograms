def logger_dec(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} \nParameters: {args}, {kwargs}" )
        return func(*args, **kwargs)
    
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

def timer_dec(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute")
        return result
    
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


@logger_dec
@timer_dec
def average(*args):
    return sum(args) / len(args)

if __name__ == "__main__":
    print(average(2, 4, 5, 10))