import random

def ins_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1

def ins_sort_rec(seq, i):
    if i==0:
        return
    ins_sort_rec(seq, i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1

rand_arr = [ random.randrange(50) for i in range(50) ]
print("iterative before: " + str(rand_arr))
ins_sort(rand_arr)
print("iterative after: " + str(rand_arr))

# resuffle
rand_arr = [ random.randrange(50) for i in range(50) ]
print("recursive before: " + str(rand_arr))
ins_sort_rec(rand_arr, len(rand_arr)-1)
print("recursiive after: " + str(rand_arr))

