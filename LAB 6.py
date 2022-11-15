#06.1.1 Speech Count

def count_vowels(string):
    count = 0

    for i in range(len(string)):
        if string[i] in "aeiouAEIOU":
            count = count + 1
    return count

string = input("Input a string: ")
print("The number of vowels contained in the string is:", count_vowels(string))


#06.1.2 Word Count

def count_words(string):
    count = 1
    pred = ""

    for i in range(len(string)):
        if string[i] in " " and pred != " ":
            count += + 1
        pred = string[i]

    if len(string) == 0:
        count = 0     
    return count

string = input("Input a string: ")
print("The number of words contained in the string is:", count_words(string))


#6.1.3 Geometric solids

from math import *

def sphere_volume(r):
    V = 4/3 * pi * r ** 3
    return V

def sphere_surface(r):
    S = 4/3 * pi * r ** 2
    return S

def cylinder_volume(r, h):
    V = pi * r ** 2 * h
    return V

def cylinder_surface(r, h):
    S = (2 * pi * r ** 2) + (2 * pi * r * h)
    return S 

def cone_volume(r, h):
    V = 1/3 * pi * (r ** 2) * h
    return V

def cone_surface(r, h):
    S = pi * r * (r + sqrt(((h ** 2) + (r ** 2))))
    return S

r = float(input('Enter the radius: '))
h = float(input('Enter the height: '))

print("The volume of the sphere is:",round(sphere_volume(r), 2),"m3")
print("The surface of the sphere is:",round(sphere_surface(r), 2),"m2")

print("The volume of the cylinder is:",round(cylinder_volume(r,h), 2),"m3")
print("The surface of the cylinder is:",round(cylinder_surface(r,h), 2),"m2")

print("The volume of the cone is:",round(cylinder_volume(r,h), 2),"m3")
print("The surface of the cone is:",round(cylinder_surface(r,h), 2),"m2")


#06.1.4 Bank Balance

def compounded_balance(y, balance, interest_rate):
    for i in range(y):
        balance = balance + balance * (interest_rate/100)
        
    return balance

y = int(input("Enter the number of years: "))
balance = float(input("Enter the initial balance: "))
interest_rate = float(input("Enter the interest rate: "))

print(f"With the interest rate of {interest_rate}%, after {y} years your balance will be {round(compounded_balance(y, balance, interest_rate),2)}$")


#06.2.1 NGOs

def ngo(income, children):
    income = float(income)
    children = int(children)

    if income <= 40000 and income >= 30000 and children >= 3:
        subsidy = children * 1000
    elif income >= 20000 and income <= 30000 and children >= 2:
        subsidy = children * 1500 
    elif income < 20000:
        subsidy = children * 2000 
    else:
        subsidy = "You are not eligible to receive any subsidy"

    return subsidy

i = 0
while i != -1:
    income = input("Enter the annual income: ")

    if income == "" :
        i = -1
    else:
        children = input("Enter the number of children: ")
        print("The financial benefit is:", ngo(income, children))
    

#6.2.2 Roman numerals

def roman_to_decimal(roman_number):
    
    if roman_number == "I":
        value = 1
    elif roman_number == "V":
        value = 5
    elif roman_number == "X":
        value = 10
    elif roman_number == "L":
        value = 50
    elif roman_number == "C":
        value = 100
    elif roman_number == "D":
        value = 500
    elif roman_number == "M":
        value = 1000

    return value 


def roman(s):
    total = 0

    while s != "":
        if len(s) == 1 or roman_to_decimal(s[0]) >= roman_to_decimal(s[1]):
            total += roman_to_decimal(s[0])
            s = s[1:]       # to remove the first character from a string
        else: 
            difference = roman_to_decimal(s[1]) - roman_to_decimal(s[0])
            total = difference + total
            s = s[2:]

    return total

s = str(input("Enter the roman number: "))
print("The converted number is:", roman(s))


#06.2.3 Aerodynamic drag

def drag(v):
    p = 1.23
    A = 2.5
    C = 0.2

    F = 0.5 * p * (v**2) * A * C
    P = F * v
    Hs = P / 745.7

    print(f'The power in watts needed to overcome the resistance of {F}N is: {P}W or {Hs}Hp')

v = float(input('Enter the speed: '))
drag(v)


#06.2.4 Electri#06.2.4 Electrical wire

from math import pi

def diameter(wire_gauge):
    d = 0.127 * (92 ** ((36 - wire_gauge) / 39))
    return d

def copper_wire_resistance(length, wire_gauge):
    p = 1.678 * 10 ** -8 
    R = (4 * p * length) / (pi * diameter(wire_gauge)**2)

    return R

def aluminum_wire_resistance(length, wire_gauge):
    p = 2.82 * 10 ** -8
    R = (4 * p * length) / (pi * diameter(wire_gauge)**2)

    return R

wire_gauge = int(input("Enter the wire gauge: "))
lenght = float(input("Enter the lenght of the wire: "))

print(f"\nThe diameter corresponding to AWG-{wire_gauge} is {round(diameter(wire_gauge), 2)}mm")

print(f"\nThe resistance of the copper wire is {round(copper_wire_resistance(lenght,wire_gauge), 6)} Ohm")

print(f"\nThe resistance of the aluminum wire is {round(aluminum_wire_resistance(lenght,wire_gauge), 6)} Ohm")