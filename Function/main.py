# global statement
# def spam():
#     global eggs;
#     eggs ="spam"
#
# eggs = 'global'
# spam()
# print(eggs)

# try catch
# def spam(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         2
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# import time, sys
#
# indent = 2  # How many spaces to indent.
# indentIncreasing = True  # Whether the indentation is increasing or not
#
# try:
#     while True:
#         print(' ' * indent, end='')
#         print('********')
#         time.sleep(0.1)  # Pause for 1/10 of a second.
#
#         if indentIncreasing:
#             indent = indent +1
#             if indent == 20:
#                 indentIncreasing = False
#
#         else:
#             indent = indent -1
#             if indent ==0:
#                 indentIncreasing = True
# except KeyboardInterrupt:
#     sys.exit()

# List
# catNames =[]
# while True:
#     print('Enter the name of cat ' + str(len(catNames) + 1) +
#           ' (Or enter nothing to stop.):')
#     names = input()
#     if not names:
#         break
#     catNames = catNames +[names]
#
# print("the cats names are:")
#
# # for i in range(len(catNames)):
# #     print(" " + catNames[i])
# for names in catNames:
#     print(" "+names)


# enumerate
# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for index, item in enumerate(supplies):
#     print("Index: " + str(index) + ", Item:" + item)
# import random
# people = ['Alice', 'Bob', 'Carol', 'David']
# random.shuffle(people)
# for human in people:
#     print(human)
people = ['Alice', 'Bob', 'Carol', 'David']
human =['Bob', 'Alice', 'Carol', 'David']
print(people == human)