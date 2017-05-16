def levenshtein(a, b):
    """ Takes two string inputs, returns an integer.
        Return value = steps needed to transform string a into string b. """
    
    # save lengths of input words
    alength, blength = len(a), len(b)
    
    # initialise empty matrix
    matrix = [[None for x in range(alength + 1)] for y in range (blength + 1)]
    
    # input: steps into 1st row (from b[0]) and column (from a[0])
    for i in range(alength + 1):
        matrix[0][i] = i
    for j in range(blength + 1):
        matrix[j][0] = j
    
    # iterating over the matrix
    for j in range (blength):
        for i in range (alength):
            # if two letters match, no substitution is required
            substitution = (0 if a[i] == b[j] else 1)
            # fill matrix indices with minimum steps to transform a into b
            # deletion, insertion, substitution
            matrix[j + 1][i + 1] = min(
                matrix[j + 1][i] + 1, 
                matrix[j][i + 1] + 1, 
                matrix[j][i] + substitution)

    # and return final matrix index!
    return(matrix[blength][alength])
