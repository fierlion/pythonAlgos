def strtoi(string_in):
    if not string_in:
        return 0
    return (int(string_in[0]) * (10 ** len(string_in)-1)) + strtoi(string_in[1:])


if __name__=='__main__':
    print strtoi('12345')
    print strtoi('')
    print strtoi('5462723124152')


