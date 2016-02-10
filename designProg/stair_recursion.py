def memo(f):
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            return f(args)
    return _f

@memo
def count_up_stairs(num_stairs):
    """a child is running up a staircase 1, 2 or 3 hops at a time
    this function returns a count of the number of ways up"""
    if num_stairs < 0:
        return 0
    if num_stairs == 0:
        return 1
    return (count_up_stairs(num_stairs-1) +
            count_up_stairs(num_stairs-2) +
            count_up_stairs(num_stairs-3))

print count_up_stairs(3)
print count_up_stairs(150)

