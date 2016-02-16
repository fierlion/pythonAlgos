def string_perms(string_in):
    result = []
    _string_perms('', string_in, result)
    return result

def _string_perms(prefix, suffix, result_arr):
    if not suffix:
        result_arr.append(prefix)
        return prefix
    else:
        mid_result = []
        for letter in suffix:
            new_prefix = letter
            mid_result.append(new_prefix)
            new_suffix = suffix.replace(letter, '')
            rec_res = _string_perms(new_prefix, new_suffix, result_arr)
            print rec_res
        print 'mid result ' + suffix
        print mid_result

if __name__ == '__main__':
    print string_perms("abc")

