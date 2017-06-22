from soundex import soundex
from levenshtein import levenshtein
from update_dict import update_dict
from create_soundexlist import create_soundexlist

# CONSTANTS
WORDLIST = './wordlist.txt'
PUNCTUATION = '''!?'":;.,/()[]{}\t\n'''

# FUNCTIONS
def correct_file():
    """ Prompts user for a .txt file, iterates over it, suggests corrections to user, and returns a corrected version of the file. """
    
    # prompt user for .txt file
    filename = input("Enter the name of the .txt file you would like to correct: ")
    if filename[-4:] != ".txt":
        return print("Function can only correct .txt files"), correct_file()
    
    # open and read contents of file
    try:
        file = open(filename, 'r')
        contents = file.readlines()
        file.close()
    except FileNotFoundError:
        print("Error: file not found.")
        return None
    
    # open new file to write corrected text to
    filename = filename.replace('.txt', '')
    new_filename = open('{}-corrected.txt'.format(filename), 'a')
    
    # for each line in file contents...
    for line in contents:
        
        # split line into words (note: we want to keep tab and newline whitespace)
        split_line = line.split(' ')
        
        for word in split_line:
            
            # select words to check spelling of
            # words with unusual non-letter characters (i.e. not punctuation) are ignored
            # words that contain non-letter characters are ignored (exception: up to one apostrophe is accepted)
            if word.strip(PUNCTUATION).replace("'", "", 1).isalpha():
                
                # assess spelling of words
                result = correct(word.strip(PUNCTUATION))
                
                # if word not found in dictionary, notify user and suggest corrections if possible
                if result != "Word appears correctly spelled!":
                    print("\nError found:", word.strip(PUNCTUATION))
                    print("Suggestions:\n" + str(result))
                    
                    # allow user to enter their preferred correction
                    correction = input("\nType in the correction desired (press enter to ignore): ")
                    
                    # if user presses enter, give them option to store word in dictionary
                    if correction == "":
                        variable = input("Do you wish to permanently remember this word? (y to accept/enter to ignore): ")
                        if variable == 'y' or variable == 'Y':
                            soundex_code = soundex(word)
                            enter(soundex_code, word)
                        pass
                    
                    # otherwise replace word with user input
                    else:
                        # replace word 
                        word = replace(word, correction)
                
                # if word found in dictionary, pass
                else:
                    pass
            
            # if letter characters are present in an otherwise invalid 'word', warn user if possible mistake
            elif word.strip(PUNCTUATION) != '' and any(c.isalpha() for c in word):
                
                print("Warning! Potential mistake found:", word.strip(PUNCTUATION), "\n")
                
                # allow user to correct or ignore
                correction = input("Enter correction if desired (press enter to ignore): ")
                
                # if enter pressed, pass
                if correction == "":
                    pass
                
                # otherwise replace word with user input
                else:
                    # replace word
                    word = replace(word, correction)
            
            # if the last character (assuming trailing punctuation) of word is a tab or newline whitespace, append it to new file
            if word[-1:] == "\n" or word[-1:] == "\t":
                new_filename.write(word)
            
            # for all other cases, append word and a space
            else:
                new_filename.write(word + ' ')
    
    # when finished, close new file and return None
    new_filename.close()
    return


def replace(word1, word2):
""" Takes two string inputs, returns a single string.
    Replaces word1 with word2 but keeps preceding and trailing punctiation. """
        
    # save preceding punctuation
    i = 0
    while i < len(word1):
        if word1[i].isalpha():
            pun1 = [char for char in word1[:i] 
                    if char in PUNCTUATION]
            break
        i += 1
    # save trailing punctuation
    j = 0
    while j < len(word1):
        if word1[len(word1) - j - 1].isalpha():
            pun2 = [char for char in word1[len(word1) - j:] 
                    if char in PUNCTUATION]
            break
        j += 1
    
    return ''.join(pun1) + word2 + ''.join(pun2)


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
