from soundex import soundex
from levenshtein import levenshtein
from create_soundexlist import create_soundexlist

# CONSTANTS
WORDLIST = './wordlist.txt'

def correct(word):
    """ Takes a string input and checks the spelling of given input.
        Returns a string notifying user if assessed as correct.
        Returns a list of possible corrections if similar words found
        Else returns None """
    
    try:
        # ensure word is alphabetic (can contain one apostrophe)
        assert word.replace("'", "", 1).isalpha()
        # ensure word or similar words exist in dictionary
        soundex_code = soundex(word)
        similar_words = sdlist[soundex_code]
    except:
        return None
    
    # sort words by levenshtein distance
    tlist = sorted((levenshtein(word.lower(), value.lower()), value) \
                    for value in similar_words)
    
    # if matching entry has distance 0, then word is correctly spelled
    if tlist[0][0] == 0 and (
        word == tlist[0][1] or 
        word[:1].lower() + word[1:] == tlist[0][1] or 
        word == tlist[1][1]):
        return "Word appears correctly spelled!"
    else:
        # return up to ten words in the list
        return [(i[1]) for i in tlist[:10]]


# MAIN PROGRAM

try:
    soundex_file = open("sdlist.txt", "r")
    sdlist = eval(soundex_file.read())
    soundex_file.close()
except:
    sdlist = create_soundexlist(WORDLIST)
