#Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. 

def findDog(phrase):
    return 'dog' in phrase.lower().split()
findDog('Is there a dog here?')