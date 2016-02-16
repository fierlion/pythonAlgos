def all_subsets(list_in):
    return _all_subsets(list_in, [], [])

def _all_subsets(list_in, prefix, result):
    if len(list_in) > 0:
        _all_subsets(list_in[1:], prefix + list_in[0:1], result)
        _all_subsets(list_in[1:], prefix, result)
        result.append(prefix+list_in[0:1])
    return result

if __name__ == '__main__':
    print all_subsets([1,2,3])
