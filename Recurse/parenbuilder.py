def parenbuilder(num_pairs):
    if num_pairs > 0:
        result = []
        pairs_doubled = num_pairs * 2
        _parenbuilder(pairs_doubled-1, 1, 0, num_pairs, '(', result)
        return result

def _parenbuilder(num_pairs, num_open, num_closed, pairs_in, cur_res, result):
    #try to open paren
    if num_open > pairs_in or num_closed > pairs_in:
        return
    if num_pairs == 0 and num_closed == num_open:
        result.append(cur_res)
        return
    if num_open <= pairs_in:
        _parenbuilder(num_pairs-1, num_open+1, num_closed, pairs_in, cur_res + '(', result)
    if num_closed < num_open:
        _parenbuilder(num_pairs-1, num_open, num_closed+1, pairs_in, cur_res + ')', result)


if __name__ == '__main__':
    print(parenbuilder(2))
    print
    print(parenbuilder(3))
    print
    print(parenbuilder(4))
