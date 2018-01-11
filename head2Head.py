'''This program creates a head-to-head rating and ranking system.
A user should be presented with two choices at random from the dictionary of items.
The user then chooses a winner, increasing the score of the winner.
All items in the dictionary can then be printed in order of their score (ranking).
'''

#each student has a score
class Student:
    def __init__(self, name, score):
            self.name = name
            self.score = score
            self.offer = (round(score*.1))
    def __repr__(self):
            return repr((self.name, self.score))

#These students are the starters
students = [
    Student('john', 1000),
    Student('jane', 1000),
    Student('dave', 1000),
    Student('jerry', 1000),
]

#function to sort the list by points and print
def printRank():
    sortedRank = sorted(students, key=lambda student: student.score, reverse = True)  # sort by score
    #print(sortedRank)
    for i in range(len(sortedRank)):
        print(i+1, '{}: {}'.format(sortedRank[i].name, sortedRank[i].score))


#function to add a student
def newStudent():
    name = input('New student\'s name: ').lower()
    score = input('Starting score. (leave blank to start at 0): ')
    if score == '':
        score = 0
    else:
        score = int(score)

    students.append(Student(name,score))
    print('Added {} with a starting score of {}'.format(name,score))    


print('\n'*20,'=====LET\'S GO HEAD TO HEAD!!!=====','\n'*5)



#=============================Add a student or play the game?=====================================

print('Add a new student or play the game?')
print('1. Add')
print('2. Play')
playChoice = input().lower()
while playChoice != '2' and playChoice != 'play':
    newStudent()
    print('\nAdd another or play?')
    print('1. Add')
    print('2. Play')
    playChoice = input().lower()

print('Current Ranking:') 
printRank()

print('\n'*4)



#Point Gainer Function
def dolePoints(winner, loser):
    winner.score += loser.offer
    loser.score -+ loser.offer
    print('\n{} lost {} points'.format(loser.name, loser.offer))
    print('{} gained {} points'.format(winner.name, loser.offer))


#choosing the players
import random




#Program loop --=-=-=-=-=-=-=-=--=- THIS RUNS THE PROGRAM
power = 1
while power > 0:
    userChoice = ''

    #Chooses a random player from the students list
    playerOne = random.choice(students)
    playerOne.offer = round(.1*playerOne.score) #Recalculte the offer for p1

    playerTwo = random.choice(students)
    playerTwo.offer = round(.1*playerTwo.score) #Recalculte the offer for p2

    number = random.randint(1,len(students)) #I don't think I need this 
    
    if playerOne != playerTwo:
        print('\nChoose a winner\n')
        print('1. {} \n\nversus \n\n2. {}'.format(playerOne.name,playerTwo.name))
        
        #User chooses a winner
        while userChoice != playerOne.name and userChoice != '1' and userChoice != playerTwo.name and userChoice != '2':
            userChoice = input().lower()   
            if userChoice == playerOne.name or userChoice == '1': #player chooses player one
                #print('chose P1') OK to remove

                
                dolePoints(playerOne,playerTwo) #Gives points to winnter, takes from loser

                print('\ndebuging:')
                print('p1', playerOne)
                print('p2', playerTwo)
                print('end debug\n')
                

                
                
            elif userChoice == playerTwo.name or userChoice == '2': #player chooses player one
                #print('chose P2') OK to remove
                
                
                dolePoints(playerTwo,playerOne) #Gives points to winnter, takes from loser

                
            elif userChoice == 'quit':
                power = 0 #ENDS PROGRAM LOOP
                break
            else:
                print('Please choose {} or {}, or type "quit" to see final scores.'.format(playerOne.name, playerTwo.name))

        continue

        

        
    else:
        continue #re-rolls players in the case of a match
    
    power = 0 #ENDS PROGRAM LOOP

print('\n'*5, '=====Finished Playing!=====', '\n'*2)
print('New Ranking:')
printRank()
print('\nProgram terminated.')

    #print('New ranking:')
    #sortedRank = sorted(students, key=lambda student: student.score, reverse = True)  # sort by score
    

    #import pprint
    #pprint.pprint(sorted(students, key=lambda student: student.score, reverse = True), width="15")   # sort by score


