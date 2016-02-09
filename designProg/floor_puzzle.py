import itertools

def floor_puzzle():
    floors = bottom, _, _, _, top = [1,2,3,4,5]
    orderings = list(itertools.permutations(floors))
    result = next((Hopper, Kay, Liskov, Perlis, Ritchie) for
            (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings
            if Hopper is not top
            and Kay is not bottom
            and Liskov is not top
            and Liskov is not bottom
            and Perlis > Kay
            and abs(Ritchie - Liskov) > 1
            and abs(Liskov - Kay) > 1)
    return list(result)

print floor_puzzle()
