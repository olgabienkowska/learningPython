class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):

    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    
    
        Student.firstName = firstName
        Student.lastName = lastName
        Student.idNumber = idNumber
        Student.scores = scores
        #print(Student.scores)
        

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(scores):
        grade = 0
        letter = ""
        for i in range (len(Student.scores)):
            grade = grade + Student.scores[i] / len(Student.scores)
        if grade >= 90:
            letter = "O"
        elif (grade >= 80) & (grade < 90) :
            letter = "E"
        elif (grade >= 70) & (grade < 80) : 
            letter = "A"
        elif (grade >= 55) & (grade < 70) : 
            letter = "P"
        elif (grade >= 40) & (grade < 55) : 
            letter = "D"
        else:
            letter = "T"
        return (letter)
            
            
   

line = input().split()