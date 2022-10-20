#03.1.1 True or False

list1 = (1, 1)

if list1[0] == list1[1]:
    print('The two values'  + str(list1) + ' are equal')
else:
    print('The two values ' + str(list1) + ' are not equal')


list2 = [1, 1.0]

if list2[0] == list2[1]:
    print('The two values ' + str(list2)+ ' are equal')
else:
    print('The two values ' + str(list2) + 'are not equal')


from math import sqrt

list3 = [2, sqrt(4)]

if list3[0] == list3[1]:
    print('The two values ' + str(list3)+ ' are equal')
else:
    print('The two values ' + str(list3) + ' are not equal')


list4= ['1', 1]

if list4[0] == list4[1]:
    print('The two values ' + str(list4) + ' are equal')
else:
    print('The two values ' + str(list4) + ' are not equal')

list5 = ['hello', 'Hello']

if list5[0] == list5[1]:
    print(str(list5) + ' The two words are the same')
else:
    print(str(list5) + ' The two words are different')


# 03.1.2 Identikit of the string

text = (input("Enter some text: "))
a = 0
b = 0

if text.isalpha():
    print ("It's a string made out of letters")
    if text.isupper():
        print('The string contains only capital letters')
    if text[0].islower():
        print('The string starts with a lowercase letter')
        if text.islower():
            print("It only contains lowercase letters")
else:
    a = True
    if text.isnumeric():
        print ("It is a string that contains only digits")
    else:
        b = True

if a and b == True:
    if text.isalnum():
        print("It is a string made of digits and letters")
    else:
        print('The string is not made of only letters and digits')

dot = "."
if text[len(text)-1] == dot:
    print('The string ends with a point')


#03.1.3 Strings and substrings

l_sequence= str(input('Enter a sequence of DNA: '))
l_sequence = l_sequence.upper()
allowed = "ACTG"

if all(ch in allowed for ch in l_sequence) and (len(l_sequence)>=20):
    s_sequence = str(input('Enter a short sequence of three characters: '))
    short = s_sequence[:3].upper()  
    long = l_sequence[:20]              #:20 to select the first 20 characters of the string

    if short in long:
        print('The short sequence is contained in the long')
        index = long.find(short)
        print('The position of the short sequence in the long is: ' + str(index))
        total = long.count(short)
        print('The short string is contained ' + str(total) + ' times in the long')
        
    else:
        print('The short sequence is not contained in the long')
else: 
    print('Enter a valid sequence')


#03.1.5 Matter of logic

x = int(input('Insert an integer value: '))

print(x > 0 and x < 100)
print(x > 0 or x < 100)
print(x > 0 or 100 < x)
print(x > 0 and x < 100 or x == -1)


#03.1.6 De Morgan

x = int(input('Insert an integer value: '))

print(' ')

print('Starting expressions: \n')

print("not (x > 0 and x < 100): " + str((not(x > 0 and x < 100)))) 

print("not (x > 0 or x < 100): " + str((not (x > 0 or x < 100))))

print("not (x > 0 or 100 < x): " + str((not (x > 0 or 100 < x))))

print("not (x > 0 and x < 100 or x == -1): " + str((not (x > 0 and x < 100 or x == -1))) + '\n\n')


print("Expressions after De Morgan's law: \n")

statement_1 = "not (x > 0 and x < 100)"
if "and" in statement_1:
    index_1 = statement_1.find('(') + 1
    x_pos = statement_1.find('a') - 1
    y_pos = statement_1.find('d') + 1
    index_2 = statement_1.find(')')
    print('not ' + statement_1[index_1:x_pos] + ' or not' + statement_1[y_pos:index_2])
else:
    index_1 = statement_1.find('(') + 1
    x_pos = statement_1.find('o') - 1
    y_pos = statement_1.find('r') + 1
    index_2 = statement_1.find(')')
    print('not ' + statement_1[index_1:x_pos] + ' and not' + statement_1[y_pos:index_2])

statement_2 = "not (x > 0 or x < 100)"
if "and" in statement_2:
    index_1 = statement_2.find('(') + 1
    x_pos = statement_2.find('a') - 1
    y_pos = statement_2.find('d') + 1
    index_2 = statement_2.find(')')
    print('not ' + statement_2[index_1:x_pos] + ' or not' + statement_2[y_pos:index_2])
else:
    index_1 = statement_2.find('(') + 1
    x_pos = statement_2.find('r') - 2
    y_pos = statement_2.find('r') + 1
    index_2 = statement_2.find(')')
    print('not ' + statement_2[index_1:x_pos] + ' and not' + statement_2[y_pos:index_2])

statement_3 = "not (x > 0 or 100 < x)"
if "and" in statement_3:
    index_1 = statement_3.find('(') + 1
    x_pos = statement_3.find('a') - 1
    y_pos = statement_3.find('d') + 1
    index_2 = statement_3.find(')')
    print('not ' + statement_3[index_1:x_pos] + ' or not' + statement_3[y_pos:index_2])
else:
    index_1 = statement_3.find('(') + 1
    x_pos = statement_3.find('r') - 2
    y_pos = statement_3.find('r') + 1
    index_2 = statement_3.find(')')
    print('not ' + statement_3[index_1:x_pos] + ' and not' + statement_3[y_pos:index_2])

statement_4 = "not (x > 0 and x < 100 or x == -1)"
if "and" in statement_4:
    index_1 = statement_4.find('(') + 1
    x_pos = statement_4.find('a') - 1
    y_pos = statement_4.find('d') + 1
    index_2 = statement_4.find(')')
    print('not ' + statement_4[index_1:x_pos] + ' or not' + statement_4[y_pos:index_2])
else:
    index_1 = statement_4.find('(') + 1
    x_pos = statement_4.find('r') - 2
    y_pos = statement_4.find('r') + 1
    index_2 = statement_4.find(')')
    print('not ' + statement_4[index_1:x_pos] + ' and not' + statement_4[y_pos:index_2])



                    #DECISIONS


#03.2.1 Trends

numbers = input('Insert three numbers: ')
numbers = numbers.split()

if numbers[0] != numbers[1] != numbers[2]:
    if numbers[0] < numbers[1] < numbers[2]:
        print('Strictly increasing')
    if numbers[0] > numbers[1] > numbers[2]:
        print('Strictly decreasing')
    else: 
        print('Neither')
else:
    print('Neither')


#03.2.2 Grades

user_grade = input('Enter the grade you want to convert: ')
grade_sign = input('Enter the sign or skip: ')
user_grade = user_grade.upper()

accepted_grades = 'ABCDF'
l = ['A', 'B', 'C', 'D', 'F']
v = [4.0, 3.0, 2.0, 1,0, 0,0]

if user_grade in accepted_grades:
    index_list = l.index(user_grade)
    value = v[index_list]
    
    if grade_sign == '+' and user_grade != 'F':
        value = value + 0.3
    if grade_sign == '-' and user_grade != 'F':
        value = value - 0.3

    print('The mark is: ' + str(value))


#03.2.3 Seasonal cycles

month = int(input('Enter the number of the month: '))
day = int(input('Enter the number of the day: '))
season = ""

if month == 1 or month == 2 or month == 3:
    season = "Winter"
elif month == 4 or month == 5 or month == 6:
    season = "Spring"
elif month == 7 or month == 8 or month == 9:
    season = "Summer"
elif month == 10 or month == 11 or month == 12:
    season = "Autumn"

if month % 3 == 0 and day >= 21:
    if season == "Winter":
        season = "Spring"
    elif season == "Spring":
        season = "Summer"
    elif season == "Summer":
        season = "Autumn"
    elif season == "Autumn":
        season = "Winter"

print("The season you are in is: " + str(season))


#03.2.4 Leap years

year = int(input('Enter the year: '))
leap = False

if (year > 1582) and (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap = True
else:
    leap = False

print('The year is leap: ' + str(leap))


#03.2.5 Grades again

user_grade = float(input('Enter the grade you want to convert: '))

if user_grade <= 4.3 and user_grade >= 0.0:
    if user_grade == 0 or user_grade < 0.5:
        print('You got F')
    if user_grade >= 0.5 and user_grade < 0.85:
        print('You got D-')
    if user_grade >= 0.85 and user_grade <= 1:
        print('You got D')
    if user_grade > 1 and user_grade <= 1.5:
        print('You got D+')
    if user_grade >= 1.5 and user_grade < 1.85:
        print('You got C-')
    if user_grade >= 1.85 and user_grade <= 2:
        print('You got C')
    if user_grade > 2 and user_grade <= 2.5:
        print('You got C+')
    if user_grade >= 2.5 and user_grade < 2.85:
        print('You got B-')
    if user_grade >= 2.85 and user_grade <= 3:
        print('You got B')
    if user_grade > 3 and user_grade <= 3.5:
        print('You got B+')
    if user_grade >= 3.5 and user_grade < 3.85:
        print('You got A-')
    if user_grade >= 3.85 and user_grade <= 4:
        print('You got A')
    if user_grade > 4 and user_grade <= 4.3:
        print('You got A+')
else:
    print('Enter a valid grade!')

#03.2.6 Taxes

income = float(input('Kindly enter your income ($): '))
married = input('Are you married? ')

if married == 'y' or 'Y' or 'yes' or 'Yes':

    if income >= 0 and income <= 16000:
        print(f'You have to pay {round((income * 0.1), 3)}$ of taxes')

    if income > 16000 and income <= 64000:
        print(f'You have to pay {1600 + round(((income-16000) * 0.15), 3)}$ of taxes')

    if income > 64000:
        print(f'You have to pay {8800 + round(((income-64000) * 0.25), 3)}$ of taxes')

else:
    if income >= 0 and income < 8000:
        print(f'You have to pay {round(income * 0.1)}$ of taxes')

    if income > 8000 and income <= 32000:
        print(f'You have to pay {800 + round(((income-8000) * 0.15), 3)}$ of taxes')

    if income > 32000:
        print(f'You have to pay {4400 + round(((income-32000) * 0.25), 3)}$ of taxes')


#03.2.7 Conversions

starting_measure = input('Enter the starting measure choosing from: ml, l, g, kg, mm, cm, m, km: ')
ending_measure = input('Enter the ending measure choosing from: fl oz, gal, oz, lb, in, ft, mi: ')
value = float(input('Enter the value to convert: '))

if starting_measure == 'ml':
    if ending_measure == 'fl oz':
        print(f'The converted value is: {round((value*0.033814), 3)} fl oz')
    elif ending_measure == 'gal':
        print(f'The converted value is: {round((value*0.000264172), 3)} gal')  
    else:
        print('Enter a valid unit of conversion!')

if starting_measure == 'l':
    if ending_measure == 'fl oz':
        print(f'The converted value is: {round((value*33.814), 3)} fl oz')
    elif ending_measure == 'gal':
        print(f'The converted value is: {round((value*0.2641718750987), 3)} gal') 
    else:
        print('Enter a valid unit of conversion!')

if starting_measure == 'g':
    if ending_measure == 'oz':
        print(f'The converted value is: {round((value*0.035274), 3)} oz')
    elif ending_measure == 'lb':
        print(f'The converted value is: {round((value*0.00220462), 3)} lb')  
    else:
        print('Enter a valid unit of conversion!')

if starting_measure == 'kg':
    if ending_measure == 'oz':
        print(f'The converted value is: {round((value*35.2739199982575), 3)} oz')   
    elif ending_measure == 'lb':
        print(f'The converted value is: {round((value*2.20462), 3)} lb')  
    else:
        print('Enter a valid unit of conversion!')

if starting_measure == 'mm':
    if ending_measure == 'in':
        print(f'The converted value is: {round((value*0.0393701), 3)} in')
    elif ending_measure == 'ft':
        print(f'The converted value is: {round((value*0.003280841666667), 3)} ft')  
    elif ending_measure == 'mi':
        print(f'The converted value is: {round((value*6.21371192237334*10**-7), 6)} mi')  
    else:
        print('Enter a valid unit of conversion!')

if starting_measure == 'cm':
    if ending_measure == 'in':
        print(f'The converted value is: {round((value*0.393701), 3)} in')
    elif ending_measure == 'ft':
        print(f'The converted value is: {round((value*0.03280841666667), 3)} ft')  
    elif ending_measure == 'mi':
        print(f'The converted value is: {round((value*6.21371192237334*10**-6), 5)} mi')  
    else:
        print('Enter a valid unit of conversion!')

if starting_measure == 'm':
    if ending_measure == 'in':
        print(f'The converted value is: {round((value*39.3701), 3)} in')
    elif ending_measure == 'ft':
        print(f'The converted value is: {round((value*3.2808388799999997), 3)} ft')  
    elif ending_measure == 'mi':
        print(f'The converted value is: {round((value*0.000621371), 4)} mi')  
    else:
        print('Enter a valid unit of conversion!')

if starting_measure == 'km':
    if ending_measure == 'in':
        print(f'The converted value is: {round((value*39370.1), 3)} in')
    elif ending_measure == 'ft':
        print(f'The converted value is: {round((value*3280.841666667), 3)} ft')  
    elif ending_measure == 'mi':
        print(f'The converted value is: {round((value*0.62137152777784099289), 2)} mi')  
    else:
        print('Enter a valid unit of conversion!')


#03.2.8 Shopping vouchers

spent = float(input('Enter the total spent: '))
voucher = 0

if spent < 10:
    print('You will not have any voucher')
elif spent >= 10 and spent <60:
    print(f'Your voucher will be worth {str(spent*0.08)}$')
elif spent >= 60 and spent <150:
    print(f'Your voucher will be worth {str(spent*0.1)}$')
elif spent >= 150 and spent <210:
    print(f'Your voucher will be worth {str(spent*0.12)}$')
elif spent > 210:
    print(f'Your voucher will be worth {str(spent*0.14)}$')


#03.2.9 Wavelengths

wavelenght = float(input('Enter the wavelenght (m): '))
print(f"{'Type': <15}{'Wavelenght (m)': ^50}{'Frequence (Hz)': >25}")
if wavelenght > 0.1:
    print(f"{'Radio Waves'}{'> 10e-1': ^70}{' < 3*10e9': >25}")

elif wavelenght <= 0.1 and wavelenght > 10**-3:
    print(f"{'Microwaves'}{'𝐹𝑟𝑜𝑚 10e-3 to 10e-1': ^60}{'𝐹𝑟𝑜𝑚 3*10e9 to 3*10e11': >5}")

elif wavelenght <= 10**-3 and wavelenght > 7*10**-7:
    print(f"{'Infrared'}{'𝐹𝑟𝑜𝑚 7*10e-7 to 10e-3': ^60}{'  𝐹𝑟𝑜𝑚 3*10e11 to 4*10e14': >5}")

elif wavelenght <= 7*10**-7 and wavelenght > 4*10**-7:
    print(f"{'Visible light'}{'𝐹𝑟𝑜𝑚 4*10e-7 to 7*10e-7': ^60}{'  𝐹𝑟𝑜𝑚 4*10e14 to 7.5*10e14': >5}")

elif wavelenght <= 4*10**-7 and wavelenght > 10**-8:
    print(f"{'Ultraviolet'}{'𝐹𝑟𝑜𝑚 10e-8 to 4*10e-7': ^60}{' 𝐹𝑟𝑜𝑚 7.5*10e14 to 3*10e16 ': >5}")

elif wavelenght <= 10**-8 and wavelenght > 10**-11:
    print(f"{'X-Rays'}{'𝐹𝑟𝑜𝑚 10e-11 to 10e-8': ^60}{'𝐹𝑟𝑜𝑚 3*10e16 to 3*10e19': >5}")

elif wavelenght <= 10**-11:
    print(f"{'Gamma rays'}{' < 10e-11': ^60}{' > 3*10e19': >5}")


#03.2.10 Back to the comet

from math import sqrt

ls = float(input('Enter a launch speed: '))

if ls < sqrt((2*(6.67*10**-11)*(2.2 * 10 **14))/4700):
    print('You will return to the surface!')
else:
    m = "{:.2e}".format(((4700*(ls**2))/((6.67*10**-11)*2)))        #"{:.2e}".format() for decimal to exponential conversion
    print('The mass of the planet to let the person return to the surface should be: ' +str(m))