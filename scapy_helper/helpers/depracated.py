def deprecated(func, *args, **kwargs):
    """
    Signal a user deprecation of specific functions
    :param func:
    :param args:
    :param kwargs:
    :return:
    """
    def wrapper():
        print("WARN:: Deprecated %s" % func.__name__)
        func(*args, **kwargs)
    return wrapper
