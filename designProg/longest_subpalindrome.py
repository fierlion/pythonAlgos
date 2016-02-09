def is_palindrome(text):
    print text, text[::-1]
    return text == text[::-1]

def longest_subpalindrome(text):
    longest = (None, None)
    #test twos then expand
    for i in range (1, len(text)):
        start = i - 1
        end = i + 1
        if is_palindrome(text[start:end]):
            while start >= 0 and end < len(text):
                start -= 1
                end += 1
                if is_palindrome(text[start:end]):
                    longest = (end - start, start)
    print longest
    #test threes then expand

print longest_subpalindrome("race ee ecar a")



