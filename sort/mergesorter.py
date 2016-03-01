def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

def mergesort(list_in):
    if len(list_in) <= 1:
        return list_in
    mid = len(list_in)//2
    left = mergesort(list_in[:mid])
    right = mergesort(list_in[mid:])
    return merge(left, right)

if __name__=='__main__':
    list = [2,5,34,1,6,3]
    print(list)
    sorted = mergesort(list)
    print(sorted)
