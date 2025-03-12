# 1.Write a decorator that counts the number of times a function has been called.
def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"{func.__name__} has been called {wrapper.count} times")
        return func(*args, **kwargs)
    wrapper.count = 0  # Initialize counter
    
    
    return wrapper

# Example usage
@call_counter
def my_function():
    print("Function is running")

my_function()
my_function()
my_function()


# 2..Write a decorator that repeats the execution of a function a specified number of times

def repeat(n):
    """Decorator to repeat the execution of a function n times."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result  # Return the last execution's result
        return wrapper
    return decorator

# Example usage
@repeat(5)
def say_hello():
    print("Hello!")

say_hello()