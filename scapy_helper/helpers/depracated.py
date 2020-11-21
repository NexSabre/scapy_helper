def deprecated(func, *args, **kwargs):
    def wrapper():
        print("WARN:: Deprecated %s" % func.__name__)
        func(*args, **kwargs)
    return wrapper
