#Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. 

def countDog(phrase):
    phrase2 = phrase.lower().split()
    count = 0
    for word in phrase2:
        if word == 'dog':
            count = count + 1
    return count

countDog('This Dog runs faster than the other dog dude!')