                            # BASIC LOOPS

#04.1.1 Integer numbers

def integer_numbers():
    n = int(input('Enter the value: '))
    number_sum = 0
    count_e = 0
    count_o = 0

    max_value = -99999999999999
    min_value = 99999999999999

    while n != "":
        n = int(n)
        number_sum = n + number_sum

        if n > max_value:
            max_value = n
        if n < min_value:
            min_value = n

        print('The partial sum is: ' + str(number_sum))
        print(f'The maximum value is {max_value} and the minimum value is {min_value}')

        if n % 2 == 0:
            count_e += 1
        else:
            count_o += 1
    
        print(f'There are {count_e} even numbers and {count_o} odd numbers')

        n = input('Enter the new value: ')

#integer_numbers()

#04.1.2 String analysis
def string_analysis():
    string_input = str(input('Enter a line of text: '))

    #capital letters
    list = []
    i = 0
    while i < len(string_input):
        if string_input[i].isupper():
            list.append(string_input[i])
        i += 1
    print(''.join(list))      # .join() to convert from list to string

    #letters in even position
    list = []
    for i in range(0, len(string_input), 2):       #jumps 2i starting from zero
        if string_input[i].isalpha():
            list.append(string_input[i])
    print(''.join(list))

    #replace vowels
    list = []
    for i in range(len(string_input)):         
        list.append(string_input[i])
        if (string_input[i] in 'aeiouAEIOU'):
            list[i] = '_'
    print(''.join(list))

    #digit count
    count = 0
    for i in range(len(string_input)):
        if (string_input[i] in '0123456789'):
            count = count + 1
    print(f'In the string there are {count} digits')

    #position of vowels
    list = []
    for i in range(len(string_input)):
        if (string_input[i] in 'aeiouAEIOU'):
            list.append(str(i))
    print('The position of the vowels in the string are: ' + ', '.join(list))

#string_analysis()

#04.1.3 Shapes
def shapes():
    number = int(input('Enter an integer number: '))

    #print cube of side 'n'
    for i in range(number):     #to create rows
        for j in range(number):     #to create columns
            print("*", end= ' ')
        print()

    print()

    #print rhombus of side 'n'

    # upward
    for i in range(number):
        for j in range(number - i - 1):
            print(' ', end='')
        for j in range(2 * i + 1):
            print('*', end='')
        print()

    # downward
    for i in range(number - 1):
        for j in range(i + 1):
            print(' ', end='')
        for j in range(2*(number - i - 1) - 1):
            print('*', end='')
        print()

#shapes()

#04.1.4 Words in reverse
def reverse_word():
    word = input('Enter a word: ')
    i = len(word) - 1
    s1 = ''

    while i >= 0:
        s1 = s1 + word[i]
        i = i - 1
    print('Reversed word: ' + s1)

    s2 = ''

    while i >= 0:
        if word[i].isupper():
            s2 = s2 + word[i]
        i = i - 1
    print('Uppercase letters of the reversed word: ' + s2)
        
#reverse_word()

#04.1.5 Prime numbers

def prime():
    n = int(input('Please enter an integer value: '))

    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                print(str(n) + " is not a prime number")
                break
        else:
            print(str(n) + " is a prime number")
    else:
        print(str(n) + " is not a prime number")

#prime()

#04.1.6 Prime numbers

def prime_under():
    maxnum =  int(input('Enter an integer value: '))

    print("The prime numbers in the range are: ")  

    for n in range(2, maxnum + 1):
        for j in range (2, n):
            if (n % j) == 0:
                break
        else:
            print(str(n))

#prime_under()

#04.1.7 Words and spaces

def substring():
    word = input("Please enter a word: ")

    for wlen in range (1, len(word) + 1):

        for i in range(len(word) - wlen + 1):
            j = i + wlen - 1
 
            for k in range(i, j + 1):
                print(word[k],end="")
            print()

#substring()

#04.1.8 Duplicate numbers

def duplicate_numbers():

    a = int(input("Enter the first number: ")) 
    b = 93506105590     # making sure the first if condition is false
                        # so the value of b can be reassigned
    list = []
    i = 0       # to count the elements in the list
    r = 0       # to count how many times a value needs to be printed

    while a != "":      # to exit in case the user presses enter
        a = int(a)
        
        if a == b and a not in list:     # check if values are equal in pairs
            list.append(a)
            i = i + 1     # if so, add 1 to the counter of the elements in the list
            if r == 0:    # if it's the first time a value needs to be printed
                r = 1     # set r to 1

        b = a                     # allows us to compare the last number of the pair             
        a = input("Enter another number: ")    # with the first one of the following

        if a != b and (len(list) > 0) and r == i:   
            print(list[i-1])    # check if two adjacent values aren't equal
            r = r + 1           # if so, check if the list contains at least one element 
                                # and then check if the number of how many times the
                                # duplicate was printed is the same as the numbers of
                                # elements in the list to avoid repetition

    l = ', '.join([str(a) for a in list])
    print('The duplicate values are:', l)

#duplicate_numbers()

#04.2.1 The game of Nim
from random import randint
from math import log2

def nim():
    marbles_total = randint(10, 100)
    player = randint(0, 1) 
    difficulty = randint(0,1)

    print("The amount of starting marbles is: " + str(marbles_total))

    while marbles_total > 0:
        print(f"{marbles_total} remaining")

        if player == 0:
            if difficulty == 0:
                if marbles_total == 1:
                    remove = 1
                else:
                    remove = randint(1, marbles_total//2)
            else:
                remove = marbles_total - 2 ** int(log2(marbles_total)) + 1
        else:
            remove = int(input("Your turn to remove: "))

        if player == 0:
            print(f"Computer removes {remove} marbles \n")
        else: 
            print(f"Player removes {remove} marbles \n")
            
        marbles_total = marbles_total - remove
        player = 1 - player

    if player == 1:
        print("The player won!")
    else:
        print("The computer won!")
        
nim()        