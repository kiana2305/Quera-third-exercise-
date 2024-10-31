def log_decorator(func):
    def wrapper(*args, **kwargs):
        # چاپ نام تابع
        print(f'Calling function: {func.__name__}')
        # چاپ پارامترها
        print(f'Arguments: args={args}')
        # اجرای تابع و ذخیره خروجی
        result = func(*args, **kwargs)
        # چاپ خروجی تابع
        print(f'Function {func.__name__} returned {result}')
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

@log_decorator
def greet(name, greeting):
    return f'{greeting}, {name}!'

@log_decorator
def factorial(n):
    output = 1
    for num in range(2, n + 1):
        output *= num
    return output

# ورودی ها
add(3, 5)
greet('Bob', 'Hi')
factorial(5)