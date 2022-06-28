#program to input user and password

# print("Who are uuu !!!")
# while True:
#     name = input()
#     if name != "Nhan":
#         print('Wrong name')
#         continue
#     print("Hello Nhan please enter your pass")
#     boolean = False
#
#     while(boolean == False):
#         password = input()
#         if(password != 'hello'):
#             print("Wrong pass")
#             continue
#         boolean = True
#     break
#
# print("Access granted")


#Truthy and Falsey
# name =''
# while not name:
#     print("Enter your fucking name bitch !!")
#     name = input()
# print("OKAy")
#
# print("Enter the number of pets")
# numbersOfPet = ''
# while not numbersOfPet:
#   print("")

#For loop
# for i in range(100):
#     if(i % 5 != 0):
#         continue
#     print(i)
# for i in range(12, 16):
#     print(i)
# for i in range(9,-1 ,-1):
#     print(i)



#ROCK, PAPER, SCISSORS
import random, sys

import random, sys
print('ROCK, PAPER, SCISSORS')
# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))

    while True: # The player input loop.
         print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
         playerMove = input()
         if playerMove == 'q':
             sys.exit()
         elif playerMove == 'r' or playerMove == 'p' or playerMove =='s':
             break
         print('Type one of r, p, s, or q.')

    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    randomNumber = random.randint(1, 3)
    computerMove =''
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1

