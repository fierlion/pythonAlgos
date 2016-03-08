import random

def quicksort(array):
    return _quicksort(array, 0, len(array))

def _quicksort(array, lo, hi):
    if hi - lo < 2:
        return
    key = random.randrange(lo, hi)
    array[key], array[lo] = array[lo], array[key]
    y = 1 + lo
    for x in range(lo + 1, hi):
        if array[x] <= array[lo]:
            array[x], array[y] = array[y], array[x]
            y += 1
    array[lo], array[y-1] = array[y-1], array[lo]
    _quicksort(array, lo, y-1)
    _quicksort(array, y, hi)


if __name__=='__main__':
    testarr = [8,4,12,4,32,1]
    quicksort(testarr)
    print(testarr)
