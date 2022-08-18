#################################################
#################################################
#                                               #
#                                               #
#                   DAY 1                       #
#                                               #
#                                               #
#################################################
#################################################


##
##def hello_world():
##    print("hello world")
##
##hello_world()
##
##
##def My_Name():
##    name = input("Hello, what Is your name? ")
##    age = int(input("and what is your age? "))
##    print(f"Your name is {name} and you are {age} years old")
##
##My_Name()    

##print(type("Hello world"))

##print(3 + 100 )
##print(1 + 2)
##print(4 / 2 )
##print(10 % 3)
##
##print("World")
##

##def who_am():
##    fName = input("Enter your first name : ")
##    sName = input("enter your last name : ")
##    print(f"hello {fName} {sName}")
##
##who_am()

##def UseingNumber():
##    number1 = float(input("Please enter the first number: "))
##    number2 = float(input("Please enter the second number: "))
##    answer = number1 + number2
##    print(f"{number1} + {number2} = {answer}")
##
##UseingNumber()

##def strings():
##    word1 = "Good"
##    word2 = "Day"
##    word3 = "John"
##
##    sentence = word1 + " " + word2 + " " + word3
##    print(sentence) ## prints the concatanated lines into one sentence
##strings()

##def IntsAndFloat():
##    number1 = input("Enter whole number: ") ## if you input a decimal number here it throws back an error as it exspects a whol number here
##    number2 = input("Enter decimal number: ")
##    
##    integer_number = int(number1) 
##    float_number = float(number2)
##    round_number = int(round(float_number)) ## this roundsdown to nearest whole number
##
##    print(number1)
##    print(number2)
##    print(round_number) ## prints the number rounded down. so if float_number is 4.8 the number will round down to 4
##
##IntsAndFloat()

##def Boolean():
##    # Boolean statemnets are used to check values to see if something is true or if something is false. 
##    name = "Pep Guardogiola"
##    age = 3
##    bark = True
##    tweet = False
##
##    print(f"My pet is called {name}, he is {age} years old") # prints the name value and age value to screen
##    print(f"Statement: {name} barks. {bark}")   # prints the name value and boolean value
##    print(f"Statement {name} tweets {tweet}")   # prints name and boolean value
##    
##Boolean()

#### Collections

##def Books():
##    books = {"Margaret Atwood":"The Handmaidens Tale", "J.R.R. Tolkien":["The Hobbit", "The Lord Of The Rings", "The Children of Hurin", "The Return Of the King" ], "Roald Dahl":"Charlie and the Chocolate Factory"}
##    authName = input("Enter an authors name : ") ## Enter J.R.R. Tolkien as teh book as there are multiple ofr that author in this code
##    print(sorted(books[authName])) ## Lists all books by author in alphibetical order
##
##Books()
##

#################################################
#################################################
#                                               #
#                                               #
#                   DAY 2                       #
#                                               #
#                                               #
#################################################
#################################################

            ################
            ## Conditions ##
            ################

##def devMoney():
##    devs_money = 100
##    dev_can_play_smash = False
##
##    if devs_money > 10 and dev_can_play_smash:
##        print("Dev enters a smash tournemnet")
##    elif devs_money < 10 and dev_can_play_smash:
##        print("Dev is too poor to enter")
##    else:
##        print("Dev just cant play smash")
##
##devMoney()

##def Conditions():
##    mark = int(input("Please enter a number: "))
##    print("--- Elif Version ---")
##    if mark >= 65 and mark < 85 :
##        print("Pass")
##    elif mark >= 85:
##        print("Distiction")
##    else:
##        print("Fail")
##
##    print("--- If only version ---")
##    if mark >= 65:
##        if mark < 85 :
##            print("Pass")
##        else:
##            print("Distinction")
##    else:
##        print("Fail")
##    
##Conditions()

        ###############
        ## Iteration ##
        ###############

##def favFilms():
##    fav_films = ["Stargate", "Star Wars", "Highlander", "Shaun Of the Dead", "Paul"]
##
##    for films in fav_films:
##        print(films.upper())
##
##favFilms()

##def WhileLoop():
##    number = 0 ## python couts 0 as 1
##    while number < 5: # while less than 5 do
##        print(number) ## This will print the number value
##        number += 1 ## this will add 1 to number until number is 5 (0 1 2 3 4)
##WhileLoop()

##def AwsomeNames():
##    number = 0
##    while number < 5:
##        name = input("What is your name? ")
##        print(f"{name} is awsome!")
##        number += 1
##AwsomeNames()

##def Range():
##    for i in range(10, 23, 2):
##        print(i) ## starting at 10 this will add 2 each time until it cant go above 23. so it will print 10 12 14 16 18 20 22
##Range()


##def ArrayPrint():
##    number = 0
##    myArray = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
##    for x in myArray:
##        print(x)
##ArrayPrint()

            ###############
            ## Functions ##
            ###############

##### this here i learned something new! didnt think return was used in python.

##def calculator(number1, number2):
##    answer = number1 + number2
##    return answer
##
##added_number = calculator(10,2)
##print(added_number + 20)

##def DefaultValues(name, greeting="hello"):
##    return f"{greeting} {name}"
##
##print(DefaultValues("steve"))
##print(DefaultValues("steve", "Good Morning"))

##def TestFunc():
##    return "Hello World"
##
##print(TestFunc())


## my version ##

##def StudentScore(name, homeWork, assessment, finalExam):
##
##    totalScore = homeWork + assessment + finalExam ## this adds all the scores together
##    finalScore = totalScore / 175 * 100 ## this calculates the overall percentage of the scores
##
##    if finalScore >= 60 and finalScore < 70: ## checks to see if percenage is between the overall score for grades
##        grade = "D"
##    elif finalScore >= 70 and finalScore < 80:
##        grade = "C"
##    elif finalScore >= 80 and finalScore < 90:
##        grade = "B"
##    elif finalScore >= 90:
##        grade = "A"
##    else:
##        grade = "Fail" ## if scores below 60% its a fail
##    
##    return f"Studant: {name}. Homework score {homeWork}/25, Assessment scor {assessment}/50, Final Exam {finalExam}/100. Percent %{finalScore}. Total grade {grade}"
##
##print(StudentScore("Steve", 25, 50, 90))
##

##def OverallScore(box1, box2, box3):
##    total = box1 + box2 +box3
##    return total/175
##
##def Percentage(decimalNumber):
##    MultBy100 = decimalNumber * 100
##    ToNearestPercent = round(MultBy100)
##    return ToNearestPercent
##
##def StringWithPercentageSymbol(Number):
##    NumberAsString = str(Number)
##    return NumberAsString + "%"
##
##def WorkOutGrade(Decimal):
##    if Decimal >= 0.85:
##        return "A"
##    elif Decimal >= 0.65:
##        return "C"
##    else:
##        return "F"
##
##homework = input("Please enter your homework score (/25): ")
##assessment = input("Polease enter your assessment score (/50): ")
##final = input("Please enter your final exam score (/100): ")
##
##homeworkFloat = float(homework)
##assessmentFloat = float(assessment)
##finalFloat = float(final)
##
##OverallDecimalScroe = OverallScore(homeworkFloat, assessmentFloat, finalFloat)
##OverallPercentageScroe = Percentage(OverallDecimalScroe)
##Result = StringWithPercentageSymbol(OverallPercentageScroe)
##
##print(f'Your overall percentage is: {Result}')
##
##grade = WorkOutGrade(OverallDecimalScroe)
##
##print(f'And your overall grade is: {grade}')
##




            ##############
            ## Moduals  ##
            ##############

##import random ## normaly imported at the top of a page
##
##roll_count = 0 ## roll count set to 0 
##
##def random_roll():
##    global roll_count ## sets global 
##    random_num = random.randint(0,20) ## this generates a random number between 0 and 20
##    roll_count += 1 ## increases the roll count variable each time
##    print(random_num) ## prints random number
##    if roll_count <= 6: ## if the roll_count is less than or equel to 6 then it will run the function again
##        random_roll() ## calling the function within the fuction
##        roll_count = 1
##
##random_roll() ## runs the function




###### test functions #####

##  this dose not work ##
##
##def TestFunc(testName):
##
##    def funcOne():
##        return f"this is func one {testName}"
##    
##
##
##    def funcTwo():
##        return "this is func two"
##    return funcTwo(), funcOne()


##
##test = TestFunc()
##test.funcTwo()

####print(TestFunc().funcOne())
##
##print(TestFunc("Testing 123"))
##


#################################################
#################################################
#                                               #
#                   DAY 3                       #
#                                               #
#               self learning                   #
#                                               #
#################################################
#################################################

######################################
##          text editing            ##
######################################

##def TextFile():
##    lines =['Hello World', 'This is a test']
##    with open('textfiles/file1.txt', 'w') as f: ## open(file, mode) file specifies the path to text file, mode specifies the mode you wish to perfom. 
##        ## modes: w opens text file for wrighting
##        ##        a opens text file to append at the end of a file
##        ##        + open text file for read and write
##        for line in lines:
##            f.write(line) ## write a string to text file
##            f.write('\n') ## starts a new line
##
##TextFile()
    
##def CustomerDetails(name, email, phonenum):
##    details = ['----------------------------------',
##               f'Customer Name: {name}',
##               f'Customer Email: {email}',
##               f'Customer Phone Number: {phonenum}',
##               '----------------------------------']
##    
##    with open('textfiles/file1.txt', 'a') as f: ## f is an alias
##        for line in details:
##            f.write(line)
##            f.write('\n')
##
##CustomerDetails('bob', 'bob@email.com', '01234789789')

##def CustomerDetails(name, email, phonenum):
##    details = ['----------------------------------',
##               f'Customer Name: {name}',
##               f'Customer Email: {email}',
##               f'Customer Phone Number: {phonenum}',
##               '----------------------------------',
##               '\n']
##    
##    with open('textfiles/file1.txt', 'a') as f: ## f is an alias
##        f.write('\n'.join(details))
##
##CustomerDetails('john', 'john@email.com', '01234789789')
##


##import os
##
##cwd = os.getcwd()
##print(cwd)
##os.chdir('C:/')
##cwd = os.getcwd()
##print(cwd)

##dir = os.path.join('C:/Users/Admin/Documents/folder5/folder6')
##print(dir)
##
##if not os.path.exists(dir):
##    os.mkdir(dir)

##cwd = os.getcwd()
##print(cwd)

##dir = os.path.join('folder2/folder3')
##print(dir)
##
##if not os.path.exists(dir):
##    os.makedirs(dir)

##def newDir(dirPath):
##    dir = os.path.join(f'{dirPath}')
##    if not os.path.exists(dir):
##        os.mkdir(dir)

##def newDirs(dirPath):
##    os.chdir(f'{dirPath}')
##    dir = os.path.join(f'{dirName}')
##    if not os.path.exists(dir)

######################################
##          decorators              ##
######################################

##def case(func, string):
##    return func(string)
##
##print(case(str.upper, "Hello World"))
##print(case(str.lower, "LOREM IPSUM"))




##def my_first_decorator(func):
##    def wrapper(name):
##        print("This is some new functionality!!")
##        return func(name)
##
##    return wrapper
##
##def greet(name):
##    return f"Hello, {name}!"
##
##greet = my_first_decorator(greet)
##print(greet("bob smith"))


##def func1(func):
##    print("this is a test")
##    print(func())
##    print("End of test")
##
##def func2(num1, num2):
##    return num1 + num2
##
##testFunc = func1(func2)
##print(testFunc(10, 20))

###### get your head around this tom!!!!!  ====^^^^^^ #######

#################################################
#################################################
#                                               #
#                                               #
#                   DAY 4                       #
#                                               #
#                                               #
#################################################
#################################################


######################################
##                Class             ##
######################################


##
##class Dog:
##    energy = "high"
##
##    def speak(self):
##        print("woof")
##
##bilbo_waggins = Dog()
##
##print(bilbo_waggins.energy)
##bilbo_waggins.speak()
##
##chewbarka = Dog()
##chewbarka.energy = "low"
##
##print(chewbarka.energy)
##chewbarka.speak()

##class Dog:
##    def __init__(self, name, breed, energy):
##        self.name = name
##        self.breed= breed
##        self.energy = energy
##
##dog1 = Dog("Bob", "Poop Monster", "High")
##print(dog1.name)

##class Student:
##    def __init__(self, name, age):
##        self.name = name
##        self.age = age
##
##John = Student("John", "21")
##Jane = Student("Jane", "22")
##
##print(getattr(John, "name"))
##print(getattr(John, "age"))

##class Student:
##    def __init__(self, name, age, _class="Student"):
##        self.name = name
##        self.age = age
##        self._class = _class
##
##    def testAve(self, score1, score2, score3):
##        totalScore = score1 + score2 + score3
##        finalScore = totalScore / 175 * 100
##        if finalScore >= 60 and finalScore < 80:
##            grade = "pass"
##        elif finalScore >= 80 and finalScore < 90:
##            grade = "merit"
##        elif finalScore >= 90:
##            grade = "Distiction"
##        else:
##            grade = "failed"
##        return f'{self.name} Scored {round(finalScore)}% overall grade {grade}'
##        #####             end of class             #####
##
##John = Student("John", "21")
##testResults = John.testAve(25, 45, 90)
##print(testResults)
##print(getattr(John, "_class"))



######################################
##               oop                ##
######################################





##class Animal:
##    babies = 0
##
##    def reproduce(self):
##        self.babies += 1
##
##class Dog(Animal):
##    def reproduce(self):
##        self.babies += 6
##
##john = Dog()
##john.reproduce()
##print(john.babies)

from abc import ABC, abstractmethod

class Bird(ABC):
    fly = True
    babies = 0

    def noise(self):
        return "Squawk"

    def reproduce(self):
        self.babies +=1

    @abstractmethod
    def eat(self):
        pass

    extinct = False

class Owl(Bird):

    def reproduce(self):
        self.babies += 6

    def eat(self):
        return "Peck Peck"

class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        return "Nom Nom"

    def reproduce(self):
        if not self.extinct:
            self.babies +=1


owlbert = Owl()
print(owlbert.eat())

dummy = Dodo()
print(dummy.eat())
print(dummy.reproduce())

##animal = input("Chose an animal. Owl or Dodo: ")
##animalName = input("What is your pets name: ")
##animalActions = input("What is the animal doing?: ")
##
##animalName = animal()
##print(animalName.animalActions())









































