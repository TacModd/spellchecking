S_GROUP = ['aeiouy', 'bfpv', 'cgjkqsxz', 'dt', 'l', 'mn', 'r']

def soundex(word):
    """ Takes a string input, returns soundex code of input as a string. """
    
    # ensure word is lower case for purpose of building soundex code
    word = word.lower()
    
    # remember first letter
    soundex_code = word[:1]
    
    # remove apostrophe for purpose of building soundex code
    word = word.replace("'", "")
    
    # remove h and w
    word = word.replace('h', '')
    word = word.replace('w', '')
    
    # initialise variable to hold letter to digit conversions
    digits = ''
    
    # replace letters in word with digits
    for letter in word[1:]:
        for i in range(0, 7):
            if letter in S_LIST[i]:
                digits += str(i)

    # remove double characters and vowels
    chars = [digits[i] for i in range(len(digits))
             if i == 0 or digits[i] != digits[i-1]]
    
    # update soundex code
    soundex_code += ''.join(chars)
    # replace 0s (vowels), append trailing 0s (in case length < 4)
    soundex_code = soundex_code.replace('0', '') + '000'
    # return soundex code
    return soundex_code[:4]
