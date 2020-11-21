def deprecated(func, *args, **kwargs):
    def wrapper():
        print(f"WARN:: Deprecated {func.__name__}")
        func(*args, **kwargs)
    return wrapper
