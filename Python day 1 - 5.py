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

##def Conditions():
##    mark = int(input("Please enter a number: "))
##    print("--- Elif Version ---")
##    if mark >= 65 and mark < 85 :
##        print("Pass")
##    elif mark > 85:
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

#### Iteration

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


##
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
















