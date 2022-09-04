from functools import wraps


def assert_print(results):
    def wrapper(func):
        @wraps(func)
        def wrapped(self, *func_args, **func_kwargs):
            import sys
            from io import StringIO

            old_stdout = sys.stdout
            sys.stdout = buffer = StringIO()

            func(self, *func_args, **func_kwargs)
            assert results == buffer.getvalue()

            sys.stdout = old_stdout

        return wrapped

    return wrapper
