# Cracking the code interview

# 1.5

def isNoRepeat():
    return False

def compressWord(word):
    if isNoRepeat():
        return word
    current_char = word[0]
    word_compressed = ''
    word_count = 1
    for i in range(1,len(word)):
        if current_char == word[i]:
            word_count = word_count + 1
        else:
            word_compressed = word_compressed + current_char + str(word_count)
            current_char = word[i]
            word_count = 1
    word_compressed = word_compressed + current_char + str(word_count)
    return word_compressed


def main():

    word1 = 'aaabbccccdddkkkkwwwjjfffffmmmmcaaaaaaaaaawff'
    comp_word = compressWord(word1)
    print comp_word

if __name__ == '__main__':
    main()


