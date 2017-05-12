def create_soundexlist(wordlist):
    """ Takes one string input which is a file location for a list of words.
        Note: assumes one word per line.
        Builds a dictionary of soundex codes in list and saves it to local directory.
        Returns the soundex dictionary as a dictionary. """
    
    # open and read file
    file = open(wordlist, 'r')
    contents = file.readlines()
    file.close()
    
    # initialise dictionary
    soundex_dict = {}
    
    # for each word, assess soundex code
    for line in contents:
        line = line.rstrip('\n')
        code = soundex(line)
        
        # enter word value into dictionary if soundex code key exists
        if code in soundex_dict:
            soundex_dict[code].append(line)
        # else enter soundex key and word value
        else:
            soundex_dict[code] = [line]
    
    # save dictionary to file
    new_file = open("sdlist.txt", "w")
    new_file.write(str(soundex_dict))
    new_file.close()
    
    # return dictionary created
    return soundex_dict
