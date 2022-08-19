import os

## three things you neee dto consider
## file
## filename
## mode
   ## r -   read
   ## w -   write
   ## r+-   read and write
   ## a -   append
## readline()   -   Reads a line
## read()       -   reads all lines
## seek()       -   navigate to location
## print(newline, file=file) this lets print write to file

## file = open("filename", "mode")

## file.close() ## always close!

##file = open("Python day 1 - 5.py", "r")
##print(file.readline(10))
##print(file.read())
##print("File Open")
##
##file.close()
##print("File Closed")

##file = open("writefiles.txt", "w")

##print(file.readline())
##file.readline(2)
##file.seek(5)
##print(file.readline())
##print(file.readline())

##lines = file.readlines()
##print(lines)

##for number in range(1, 11):
##    newline = "this is a line " + str(number) + "\n"
##    file.write(newline)
##
##file.close()


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

def SportsTeams(team1, team2, team3, team4, team5):
    details = [f'{team1}',
               f'{team2}',
               f'{team3}',
               f'{team4}',
               f'{team5}',
               ]
    
    with open('textfiles/sportsteams.txt', 'w') as f: ## f is an alias
        f.write('\n'.join(details))

    teams = open('textfiles/sportsteams.txt', 'r')
    print(teams.readline())
    teams.readline()
    teams.readline()
    print(teams.readline())


SportsTeams('liverpool', 'manchester united', 'everton', 'leeds united', 'manchester city')

def SportsTeams(team1, team2, team3, team4, team5):
    details = [f'{team1}',
               f'{team2}',
               f'{team3}',
               f'{team4}',
               f'{team5}',
               ]
    
    with open('textfiles/sportsteams.txt', 'w') as f: ## f is an alias
        f.write('\n'.join(details))

    with open('textfiles/sportsteams.txt', 'r') as teams:
        print(teams.read())


SportsTeams('this is a new line', 'manchester united', 'everton', 'leeds united', 'manchester city')











