import os
import re
from soundex import soundex
from levenshtein import levenshtein
from create_soundexlist import create_soundexlist

# CONSTANTS
WORDLIST = './wordlist.txt'



def search_files(dirname='./documents', search_term=None, autocorrect=1):
    """ Searches for entered term(s) within files in a given directory, and prints sentences with matching terms.
        Has automatic spellchecking and correction for term(s) entered (enabled by default but can be disabled).
        Function takes up to 3 arguments:
        dirname is a string, the search directory. Set to 'documents' folder in current directory by default.
        search_term is a string, the search term. If no search term is entered, user will be prompted for one.
        autocorrect is an integer, with default value 1 to enable autocorrection of entered term. Set to 0 to disable.
        Returns None """
    
    # ensure dirname exists
    if not os.path.isdir(dirname):
        print("Error: search directory does not exist.")
        return None
    
    # prompt user for search term (if string not passed by argument to function)
    if type(search_term) != str:
        search_term = input("Enter a word you would like to search: ")
    
    # declare a variable result that will be used for later reference
    result = None
    
    # if only one search term entered...
    if not ' ' in search_term and not '\t' in search_term:
        # if spellchecking disabled, assume word is spelled correctly
        if autocorrect == 0:
            result = "Word appears correctly spelled!"
        
        # if enabled, check spelling of single word
        else:
            # ignore capitalisation
            result = correct(search_term[:1] + search_term[1:].lower())
            
            # if term not recognised, autocorrect to closest match
            if type(result) == list:
                original_term = search_term
                search_term = result[0]
    
    # otherwise more than one term is entered
    else:
        # split phrase into list
        search_list = search_term.split()
        
        # if spellchecking disabled, assume words are spelled correctly
        if autocorrect == 0:
            result = "Word appears correctly spelled!"
        
        # if enabled, checking spelling of each word
        else:
            # remember original search in case search_term is altered
            original_term = search_term
            
            for term in search_list:
                # need a local result variable for each word
                local_result = correct(term[:1] + term[1:].lower())
                
                # if not recognised, autocorrect and update search term & list
                if type(local_result) == list:
                    result = local_result
                    search_term = search_term.replace(term, local_result[0])
                    search_list.remove(term)
                    search_list.append(local_result[0])

    # for each file in the directory given...
    for filename in os.listdir(dirname):
        
        # open file, read & split contents into sentences
        file = open('{}/{}'.format(dirname, filename))
        contents = file.read()
        contents = contents.replace('\n', '.')
        sentences = contents.split('.')
        file.close()
        
        # intialise a count and an output variable
        output = ''
        
        # if more than one search term...
        if ' ' in search_term or '\t' in search_term:
            
            # initialise a count variable
            sentence_count = 0
            
            # create a local copy of the list of search terms
            local_list = list(search_list)
            
            # for each sentence within each file contents...
            for sentence in sentences:
                
                # strip whitespace
                sentence = sentence.strip()
                
                # create an extra local copy
                # lets the program highlight all terms in the same sentence
                xtra_local_list = list(local_list)
                
                # initialise a signal variable
                signifier = 0
                
                # for each term in the most local copy of the list...
                for term in xtra_local_list:
                    
                    # search for term (whole word only, not substrings)
                    if re.search(r'\b{}\b'.format(term), sentence, flags=re.I):
                        
                        # if found, update sentence to highlight term
                        sentence = re.sub(r'\b{}\b'.format(term), term.upper(), sentence, flags=re.I)
                        
                        # remove term so as not to search for it twice
                        # note: removes from local_list to avoid skipping terms in the same sentence
                        local_list.remove(term)
                        
                        # update signifier variable to reflect term found
                        signifier = 1

                
                # if a term is found in sentence...
                if signifier == 1:
                    
                    # append sentence to output and update sentence_count
                    output += sentence
                    sentence_count += 1
                    
                    # while output < 3 sentences, append newline character
                    if sentence_count < 3:
                        output += '... '
                    
                    # if output >= 3 sentences, end search (even if more than 3 search terms)
                    else:
                        output += ' ...'
                        break
        
        # otherwise if only one term...
        else:
            
            # for each sentence within each file contents...
            for sentence in sentences:
                
                # strip whitespace
                sentence = sentence.strip()
            
                # search for term
                if re.search(r'\b{}\b'.format(search_term), sentence, flags=re.I):
                
                    # if found, append sentence to output (with term highlighted)
                    output += re.sub(r'\b{}\b'.format(search_term), search_term.upper(), sentence, flags=re.I)
                    break
        
        # is search term(s) is not found in file, pass
        if output == '':
            pass
        
        # if it is found, print results to screen
        else:
            print("\nIn {}:".format(filename) + "\n{}\n".format(output))
    
    # if user's input was autocorrected, let user rerun search with original term
    if type(result) == list:
        print("\nDisplaying results for {}.\n".format(search_term))
        
        # loop will end when user answers properly
        ans = None
        while ans not in ['Y','y','N','n']:
            ans = input("Search for {} instead? y/n: ".format(original_term))
            
        # if yes answered, run function again with autocorrect disabled
        if ans == 'y' or ans == 'Y':
            return search_files(search_term=original_term, autocorrect=0)
            
        # otherwise pass and allow function to exit
        else:
            pass
    
    # when search finished, return None
    return None



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
    sdlist = build_sdex_list(WORDLIST)
