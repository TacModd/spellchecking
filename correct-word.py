from correct import correct
from create_soundexlist import create_soundexlist

# CONSTANTS
WORDLIST = './wordlist.txt'


# MAIN PROGRAM

try:
    soundex_file = open("sdlist.txt", "r")
    sdlist = eval(soundex_file.read())
    soundex_file.close()
except:
    sdlist = create_soundexlist(WORDLIST)
