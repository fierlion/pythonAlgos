def rec_reverse(string_in):
    if not string_in:
        return string_in
    else:
        return string_in[-1] + rec_reverse(string_in[:-1])
if __name__ == '__main__':
    print(rec_reverse('reversed'))
    print(rec_reverse(''))
