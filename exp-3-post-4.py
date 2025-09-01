#find longest word in a string
def find_longest_word(s):
    words = s.split()
    longest_word = max(words, key=len)
    return longest_word