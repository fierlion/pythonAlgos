def ksubsets(list_in, k):
    return _all_subsets(list_in, [], [], k)

def _all_subsets(list_in, prefix, result, k):
    if len(list_in) > 0:
        if len(prefix) < k:  # prune branch if too long
            _all_subsets(list_in[1:], prefix + list_in[0:1], result, k)
            _all_subsets(list_in[1:], prefix, result, k)
            this_result = prefix + list_in[0:1]
            if len(this_result) == k:  # don't prune if too short
                result.append(this_result)
    return result

if __name__=='__main__':
    print(ksubsets([1,2,3], 3))
