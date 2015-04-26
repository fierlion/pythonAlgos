import random
import time

def gnomesort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] < seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1

def mergesort(seq):
    mid = len(seq)//2
    lft, rgt = seq[:mid], seq[mid:]

    if len(lft) > 1:
        lft = mergesort(lft)
    if len(rgt) > 1:
        rgt = mergesort(rgt)

    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res


shuffd_seq = [i for i in range(5000)]
random.shuffle(shuffd_seq)

start = time.time()
gnomesort(shuffd_seq)
end = time.time()
print(end - start)

random.shuffle(shuffd_seq)
start = time.time()
mergesort(shuffd_seq)
end = time.time()
print(end - start)
