def all_subsets(list_in):
    result_set = set()
    first_tuple = tuple(list_in)
    last_tuple = first_tuple[-1:]
    result_set.add(first_tuple)
    result_set.add(last_tuple)
    _all_subsets(first_tuple, result_set)
    return [list(tup) for tup in result_set]

def _all_subsets(tuple_in, set_in):
    if not tuple_in:
        return
    window_length = len(tuple_in)-1
    for i in range(len(tuple_in)-1):
        window_slice = tuple_in[i:i+window_length]
        set_in.add(window_slice)
        _all_subsets(window_slice, set_in)

if __name__ == '__main__':
    print(all_subsets([1,2,3,4,5]))
    print(all_subsets([]))
    print(all_subsets([1]))
