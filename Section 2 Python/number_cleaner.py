
#assumes South African, codeless mobile number
def numberCleaner(dirtyNumber):

    #remove white spaces
    spacelessString = dirtyNumber.strip().replace(" ", "")

    #remove all non numeric characters
    numericString = ''.join(character for character in spacelessString if character.isdigit())

    #check if first character is a zero0
    if numericString[0] != '0':
        numericString = '0' + numericString
    #if length is 10, throw exception else return number    
    if len(numericString) == 10:
        return numericString
    else :
        raise Exception("The number provided was of invalid length")


    

