def S(seq, i=0):
    if i == len(seq):
        return 0
    return S(seq, i+1) + seq[i]

def cost_S(seq, i=0):
    if i == len(seq):
        return 1
    return cost_S(seq, i+1) + 1

for n in range(100):
    seq = range(n)
    assert cost_S(seq) == n+1

sequence = range(1,101)
print(S(sequence))
print(cost_S(sequence))
