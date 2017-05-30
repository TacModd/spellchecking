def update_dict(soundex_code, word):
    """ Takes two string inputs: a soundex code key and a corresponding word value.
        Enters input into local soundex dictionary and returns None. """
    
    # if soundex key already in dictionary, update list of word values for that key
    if soundex_code in sdlist:
        new_values = sdlist[soundex_code]
        new_values.append(word)
        sdlist[soundex_code] = sorted(new_values)
    
    # otherwise enter new soundex key and word value
    else:
        sdlist[soundex_code] = [word]
    
    # save updated dictionary
    new_file = open("sdlist.txt", "w")
    new_file.write(str(sdlist))
    new_file.close()
    
    return None
