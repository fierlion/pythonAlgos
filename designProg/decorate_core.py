def n_ary(f):
    def n_ary_f(x, *args):
        print x, args
        return x if not args else f(x, n_ary_f(*args))
    return n_ary_f

@n_ary
def add(x, y):
    return x + y

print add(1,2,3,4)
