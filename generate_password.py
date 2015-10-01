
import random

def createPassKeyOrdinals():
    '''
    returns a list of ordinal values of all ACII letters
    numbers and some odd characters like !#$%&
    '''
    lowers = list(range(97, 123))
    uppers = list(range(65, 91))
    numbers = list(range(48, 58))
    odds = [33, 35, 36, 37, 38]
    return lowers + uppers + numbers + odds


def getPassKey(length, ordinals):
    ''' returns a random passkey/password of given length '''
    # shuffle the ordinals in place
    random.shuffle(ordinals)
    # slice off a list of a given length
    myOrdinals = ordinals[0:length]
    # convert to a string
    return "".join(chr(n) for n in myOrdinals)


# testing ...
ordinals = createPassKeyOrdinals()
# set length of key
length = 20
for k in range(6):
    myKey = getPassKey(length, ordinals)
    print(myKey)
