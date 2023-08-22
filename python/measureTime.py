import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken by {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@measure_time
def slow_function(n):
    total = 0
    for i in range(n):
        total += i
        time.sleep(0.1)  # Simulate a slow operation
    return total

slow_function(5)
