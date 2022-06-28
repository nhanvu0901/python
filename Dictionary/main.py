# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
#
# while  True:
#     print("Enter the name you want to find")
#     name = input()
#     if not name:
#         break
#     elif name in birthdays:
#         print(birthdays[name]+ ' is the birthday of '+name)
#     else:
#         print("We don't have the name in the database")
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] =bday
#         print('Birthday database updated.')

# Count the word
# import pprint
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
# for character in message:
#     if character not in count:
#         count[character] = 1
#     else:
#         count[character] +=1
#
# pprint.pprint(count)






# tic tac toe
# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
#
#
# def checkWin(turn):
#     pos = []
#     flag = False
#     for k in theBoard.keys():
#         if theBoard[k] == turn:
#             pos.append(k)
#
#     if 'top-L' in pos and 'top-M' in pos and 'top-R' in pos:
#         flag = True
#         return flag
#
#     elif 'top-L' in pos and 'mid-M' in pos and 'low-R' in pos:
#         flag = True
#         return flag
#     elif 'top-L' in pos and 'mid-M' in pos and 'low-R' in pos:
#         flag = True
#         return flag
#     elif 'top-L' in pos and 'mid-M' in pos and 'low-R' in pos:
#         flag = True
#         return flag
#
#     elif 'top-L' in pos and 'mid-M' in pos and 'low-R' in pos:
#         flag = True
#         return flag
#     elif 'top-L' in pos and 'mid-M' in pos and 'low-R' in pos:
#         flag = True
#         return flag
#     elif 'top-L' in pos and 'mid-M' in pos and 'low-R' in pos:
#         flag = True
#         return flag
#
#     elif 'top-L' in pos and 'mid-M' in pos and 'low-R' in pos:
#         flag = True
#         return flag
#
#     elif ' ' not in theBoard.values():
#         return False
#     else:
#         return ''
#
#
# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
#
#
# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print("It is " + turn + " please select move")
#     move = input()
#     theBoard[move] = turn
#     if checkWin(turn) == True:
#         print(turn+" win the game")
#         break
#     if checkWin(turn) == False:
#         print('It is a draw')
#     if turn == 'X':
#         turn = '0'
#     else:
#         turn = 'X'
#
# printBoard(theBoard)


# Practice
def addToInventory(inventory, addedItems):
    for key, value in list(inventory.items()):
        for item in addedItems:
            if key == item:
                inventory[key] += 1

            if item not in inventory:
                inventory[item] = 1

    return inventory


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
