def all_subsets(iterable):
    s = tuple(iterable)
    for size in range(1, len(s)+1):
        for index in range(len(s)+1-size):
            yield iterable[index:index+size]

if __name__ == '__main__':
    subsets = all_subsets([1,2,3])
    for sset in subsets:
        print sset
