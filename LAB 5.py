#05.1.1 ATM

def atm():
    pin = '1234'
    n = 1

    while n <= 3:
        user = input('Please enter the PIN: ')
        
        if user == pin:
            print('Your PIN is correct')
            break
        else:
            print('Your PIN is incorrect')
        
        if n == 3:
            print('\nYour bank card is blocked')
            
        n = n + 1

#atm()

#05.1.2 Noms des pays

def pays():
    milst = ["Belize", "Cambodge", "Mexique", "Mozambique", "Zaïre", "Zimbabwe"]
    plist = ["Etats-Unis", "Pays-Bas"]
    vowels = ["A", "E", "I", "O", "U"]

    country = str(input("Enter a french country name: "))
    country = country.capitalize()

    dash = country.find("-")

    countrytwo = country[dash + 1:]
    countrytwo = countrytwo.capitalize()

    country = country[:dash + 1] + countrytwo

    if country[len(country)-1] == "e" and country not in milst and country not in plist:
        if country[0] in vowels and country not in plist:
            print(f"L' {country}")
        else: 
            if country in plist:
                print(f'Les {country}')
            else:
                print(f'La {country}')
    else: 
        if country[0] in vowels and country not in plist:
            print(f"L'{country}")
        else:
            if country in plist:
                print(f'Les {country}')
            else:
                print(f'Le {country}')
#pays()

#05.1.3 Factoring of integers

def factoring():       # to have all prime factors of a number

    from math import sqrt

    num = int(input('Enter an integer value to factor: '))

    while num % 2 == 0:   # print the twos that divide num
        print(2)
        num = num / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(sqrt(num))+1, 2):
        while num % i== 0:
            print(i),
            num = num / i
             
    if num > 2:       #then it is a prime number only if num > 2
        print(int(num))

#factoring()    

#05.1.4 At cinema

def cinema():
    tickets = 10
    buyers = 0

    while tickets > 0:
        buy = int(input('How many tickets to buy: '))

        if (buy > 0 and buy <= 4 and tickets >= buy):
            tickets = tickets - buy
            buyers = buyers + 1
        else: 
            print('Enter a valid number of tickets')

        print(f'There are {tickets} tickets left')

        if tickets == 0:
            print(f'\nThere were {buyers} buyers!')

#cinema() 

#05.2.1 Random generator

def generator():

    a = 32310901
    b = 1729
    m = 224
    r = int(input('Enter a number: '))

    i = 0

    while i < 10:
        R = (a * r + b) % m
        print(R)

        r = R
        i = i + 1

#generator()

#05.2.2 The Drunkard’s Walk

def drunkard():

    from random import choice

    (x,y) = (0,0)

    directions = ['N', 'S', 'E', 'W']
    for i in range(100):    
        a = choice(directions)
          # random.choice to choose a random element in a LIST
        if a == 'N':
            y = y + 1
        elif a == 'S':
            y = y - 1
        elif a == 'E':
            x = x + 1
        else:
            x = x - 1
                
    print(f'Ending position: ({x},{y})')

#drunkard()

#05.2.3 Predator-prey simulation

def simulation():

    # A = 0.1     # growth rate prey
    # B = 0.01    # rate of prey destruction
    # C = 0.01    # mortality rate predators
    # D = 0.00002 # predators increase rate

    A = float(input('Enter the growth rate of the prey: '))
    B = float(input('Enter the rate of prey destruction: '))
    C = float(input('Enter the mortality rate of predators: '))
    D = float(input('Predator increase rate: '))

    # x = 1000     # prey population
    # y = 20    # predators population

    x = int(input('Enter the prey population: '))
    y = int(input('Enter the predators population: '))

    periods = int(input('Enter the number of periods: '))

    for i in range(1, periods + 1):
        x = x * (1 + A - B * y)
        y = y * (1 - C + D * x)

        print("\nAfter period", i, "there are", round(y), "predators and", round(x), "prey")

#simulation()

#05.2.4 Electrical transformers
def transformer():

    n = 0.01
    r = 20
    R = 8
    V = 40
    p = -9223372036854775807    

    while n < 2.01:
        P = R * ((n * V)/((n ** 2) * r + R)) ** 2

        print(f"At the turn ratio of {round(n,2)}, the power delivered is {round(P,5)}W \n")
        
        if p < P:
            p = P
            N = n

        n += 0.01
    
    print(f"\nThe highest power delivered is {round(p, 5)}W, obtained with a {round(N, 2)} turn ratio")
    
#transformer()