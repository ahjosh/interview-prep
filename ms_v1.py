

def printText(text, n):
    str1 = []
    str_rest = []
    counter = 0


#    for ind1 in range(len(text)):

def isPalindrome(word):
    print word
    if len(word) < 2:
        return True
    
    if word[0] == word[-1]:
        #print word
        return isPalindrome(word[1:-1])
    else:
        return False
def removeChar(word, char):
    word_ptr = list(word)

def recPermute(prefix,rest):
    if not rest:
        print prefix

    for ind in range(len(rest)):
        str1 = prefix+rest[ind]
        str2 = rest[:ind]+rest[ind+1:]
        recPermute(str1,str2)

def ListPermutation(word):
    recPermute('',word)
    
    
        
        
def main():
    
    ListPermutation('ABC')
    while False:
        str_input = raw_input('Word to check (Enter to exit): ')
        if not str_input:
            break
        if isPalindrome(str_input):
            print str_input + ' is palyndrome.'
        else:
            print 'No, '+str_input + ' is not palyndrome.'

if __name__ == '__main__':
    main()

