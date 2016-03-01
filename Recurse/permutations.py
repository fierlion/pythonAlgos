def all_perms(elements):
    if len(elements) == 2:
        yield elements
    else:
        for i in xrange(len(elements)):
            for perm in all_perms(elements[:i] + elements[i+1:]):
                yield elements[i:i+1] + perm


if __name__ == '__main__':
    perms = all_perms([1,2,3,4])
    for perm in perms:
        print perm
