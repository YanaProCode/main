def get_longest_word( s: str) -> str:
    words_list = s.split(' ')
    count = 0
    longest_word = ''
    for word in words_list:
        word = word.strip(' ')
        word = word.strip('\n')
        word = word.strip('\t')
        if len(word) > count:
            count = len(word)
            longest_word = word
        else:
            continue
    return longest_word
