#07.1.1  Sum  with  alternating  signs

def alternating_sum():
    s = input("Please input a sequence of integers separated by a space: ")
    s_list = []
    total = 0

    s_list = s.split(" ")
    print(s_list)

    for i in range(len(s_list)):
        print(s_list[i], end = " ")
        if i % 2 == 0:
            total = total + int(s_list[i])
            if i != (len(s_list) - 1):
                print("-", end = " ")
        else: 
            total = total - int(s_list[i])
            if i != (len(s_list) - 1):
                print("+", end = " ")

    print("=", total)

alternating_sum()


#07.1.2  List  of  random  numbers
from random import randint

def random_list():

    values = []

    for i in range(0, 10):
        values.append(randint(1, 100))

    print("Elements at even index:", end=" ")
    for i in range(0, len(values), 2):
        print(values[i], end=" ")

    print("\nElements that have equal value:", end=" ")
    for i in range(len(values)-1):
        if values[i] == values[i+1]:
            print(values[i], end=" ")
    
    print("\nIn reverse order:", end=" ")
    for val in values[::-1]:
        print(val, end=" ")

    print(f"\nThe first element is {values[0]} and the last element is {values[-1]}")

random_list()


#07.1.3 Remove the minimum value

def remove_min(v):
    min_value = v[0]

    for i in range(len(v)):
        if v[i] < min_value:
            min_value = v[i]
        
    position = v.index(min_value)
    v.pop(position)

    print("The minimum value is:", min_value)
    print("The new list is:", str(v))

remove_min([10, 22, 232, 42, 25, 653, 72, 82, 9, 11])


#07.1.4 Local highs

def local_highs():
    count = 0
    integers = []
    
    new_int = " "
    
    while new_int != "":
        new_int = input("Enter an integer value: ")
        if new_int != "":
            integers.append(int(new_int))
    
    print(integers)
    

    maxima_position = []
    
    for i in range(1, len(integers)-1):
        if integers[i] > integers[i+1] and integers[i] > integers[i-1]:
            maxima_position.append(i)
            count += 1

    if count == 0:
        print("There are no local maxima")
    else:
        maxima_joined = ", ".join(map(str, maxima_position))
        print("The local maxima are in position:", maxima_joined)
        print("There are " + str(count) + " local maxima")

        if count > 1 :
            two_maxima = []

            closest = maxima_position[1] - maxima_position[0]
            value_index = 0

            for x in range(len(maxima_position)-1):
                diff = maxima_position[x+1] - maxima_position[x]
                if diff < closest:
                    closest = diff
                    value_index = x
            two_maxima.append(maxima_position[value_index])
            two_maxima.append(maxima_position[value_index+1])

            two_joined = ", ".join(map(str, two_maxima))
            print("The two closest local maxima are:", two_joined)

local_highs()


#07.1.5 The same elements
    
def same_set(a,b):

    equalA = True
    equalB = True

    for value in a:
        if value not in b:
            equalA = False
    
    for value in b:
        if value not in a:
            equalB = False

    if equalA == True and equalB == True:
        print("The two lists contain the same elements")
    else:
        print("The two lists DON'T contain the same elements")
        
same_set([1, 4, 9, 16, 9, 7, 4, 9, 11], [11, 11, 7, 9, 16, 4, 1])


#07.1.6 Ordered list

from random import randint

def ordered_list():
    total_values = 20
    starting_list = []

    for i in range(total_values):
        starting_list.append(randint(0,99))
    
    print("The starting list is:", starting_list)

    starting_list.sort()
    print("The sorted list is:", starting_list)

ordered_list()


#07.1.7 Add up without the minimum

def sum_without_smallest(v):
    sum = 0
    i = 1

    while i < len(v):
        sum += v[i]
        i += 1
    
    print("The sum of the values in the list (excluding the first) is:", sum)

sum_without_smallest([1, 4, 9, 16, 9, 7, 4, 9, 11])



            ###     Part 2 – Algorithms that make use of lists


        
#07.2.1  Measurement  noise

def noise():
    list_noise = [1.1212, 1.1211, 1.2241, 1.1322, 1.1421, 1.1223, 1.4221, 1.2321, 1.1632]

    print("First values:\n" + str(list_noise))

    # Handle the first element in the list
    old_left = list_noise[0]
    list_noise[0] = (list_noise[0]+list_noise[1]) / 2

    # Handle all values except the first and the last
    for i in range(1, len(list_noise)-1):
        current = list_noise[i]
        list_noise[i] = (old_left + list_noise[i] + list_noise[i + 1]) / 3
        old_left = current

    # Handle the last element in the list
    list_noise[len(list_noise) - 1] = (old_left + list_noise[len(list_noise) - 1]) / 2

            #list_noise = [f"{n:.3f}" for n in list_noise]
    list_noise = [round(n, 4) for n in list_noise]

    print("Smooth values:\n" + str(list_noise))

noise()


#07.2.2  Distances

def RowPicker(row_lenght, spots):   
    count_free = 0
    max_free = 0

    for i in range(row_lenght):      

        # Check whether an element is considered a free spot
        if spots[i] == "_":
            if count_free == 0: 
                count_starting = i

            count_free += 1
            if count_free > max_free:
                max_free = count_free
                max_starting = count_starting

        else:
            count_free = 0
            
    return max_free, max_starting


def distances_main(row_lenght):

    spots = []
    spots = ["_"] * row_lenght     # Create the parking lot
    
    for i in range(row_lenght):
        if i != 0: 
            max_free, max_starting = RowPicker(row_lenght, spots) # Tuple with: 0 = max_free // 1 = max_starting

                # If there is more than one spot left, park the car 
                # in the middle of the largest space between cars

            if max_free > 1:   # if the number of free spots is > 1 
                spots[max_starting + int(max_free / 2)] = "X"

            # Fill the remaining spots starting from the left
            else:   
                spots[max_starting] = "X"

            # First, park the car in the middle of the parking lot
        else:   
            place_X = int(row_lenght / 2)
            spots[place_X] = "X"
        
        print(spots)
        
row_lenght = int(input("Enter the number of spots: "))
distances_main(row_lenght)


#07.2.3 Bulgarian solitaire

from random import randint

def bulgarian_solitaire():
    cards = 45
    piles_number = randint(1,45)

    board = []

    for i in range(piles_number):
        random_number = randint(0,cards)

        if random_number != 0:
            board.append(random_number)
            cards -= random_number

    print("The starting board is:\n" + str(board))
    print()

    if board != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        while board != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            count = 0
            
            for i in range(len(board)):
                board[i] = board[i] - 1
                count += 1

            board_lenght = len(board)
            
            element = 0
            while element < board_lenght:
                if board[element] < 1:
                    board.pop(element)

                    element = 0
                    board_lenght = len(board)
                else:
                    element += 1
            
            board.append(count)
            
            print(board)

    else:
        print(board)

bulgarian_solitaire()