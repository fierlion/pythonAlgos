def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, looks up value in cache"""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args isn't hashable
            return f(args)
    return _f

#test using naive fibonacci
@memo
def fib(n): return 1 if n <= 1 else fib(n-1) + fib(n-2)

print fib(100)
