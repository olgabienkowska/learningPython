if __name__ == '__main__':
    n = int(input())
        
myPhoneBook = {"": ""}

for i in range(n):
    if __name__ == '__main__':
        phoneBook = str(input())
        
    myNumber = int((phoneBook[-9:]))
    myName = str((phoneBook)[0:-9])

    myPhoneBook[myName] = myNumber
  

for i in range(n):
    if __name__ == '__main__':
        phoneBook = str(input())
    
    if phoneBook in myPhoneBook:
        description = myPhoneBook.get(phoneBook)
        print("{}={}".format(phoneBook,description))
    else:
        print("Not found")