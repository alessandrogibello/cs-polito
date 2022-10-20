#02.1.1 Two numbers

a = int(input('Insert the first number: '))
b = int(input('Insert the second number: '))

def sum():   
    sum = a+b
    print('The sum of the two numbers is: ' + str(sum))

def diff():    
    diff = a-b
    print('The difference between the two values is: ' + str(diff))

def product():
    prod = a*b
    print('The product of the two numbers is: '+ str(prod))

def avg():
    avg = float((a+b)/2) 
    print('The average value is: ' + str(avg))

def distance():
    dist = a-b
    print('The distance is: ' + str(abs(dist)))

def maximum():
    maxx = max(a,b)
    print('The maximum between the values is: ' + str(maxx))

def minimum():
    minn = min(a, b)
    print('The minimum between the values is: ' + str(minn))


sum()
diff()
product()
avg()
distance()
maximum()
minimum()

#02.1.2 Resistances

r1 = float(input('Insert the value of the first resistance in your circuit: '))
r2 = float(input('Insert the value of the second resistance in your circuit: '))
r3 = float(input('Insert the value of the third resistance in your circuit: '))

def resistance():
    res = r1 + ((1/r2)+(1/r3))
    print('The resistance of the circuit is: ' + str(res)+ ' Ohm')

resistance()



#02.1.3 Digits

num = int(input('Insert the number you want to display the individual digits: '))

def individual():
    if(num in range(10000,99999)):
        c1 = int(num/10000)
        c2 = int((num%10000)/1000)
        c3 = int((num%1000)/100)
        c4 = int((num%100)/10)
        c5 = int((num%10))
        print('The individual digits are: ' + str(c1) + ' ' + str(c2) + ' ' + str(c3) + ' ' + str(c4) + ' ' + str(c5))
    else: (print('Insert a value in the interval between 10000 and 99999'))

individual()

#02.1.4 Hybrid car

price = float(input('Insert the price of the car: '))   
total_km = int(input('Insert the amount of estimated km made in a year: '))
fuel_cost = float(input('Insert the estimate of the cost of the fuel: '))
efficiency = float(input('Insert the efficiency of your engine (km/l): '))
resale_value = int(input('Insert the resale value of the used car after 5 years: '))

def cost():
    car_cost = (price - resale_value)+((total_km/efficiency)*fuel_cost*5)
    print('The cost of your car is: ' + str(car_cost))

cost()

#02.1.5 Electric force

from cmath import pi

q1 = float(input('Insert the value of the charge (C) of the first particle: '))
q2 = float(input('Insert the value of the charge (C) of the second particle: '))
r = float(input('Insert the distance (m) between the two particles:'))

def force():
    el_force = (q1*q2)/(4*pi*0.000000000008854*(r*r))
    print('The electrical force between the two particles is: ' +str(el_force)+' N')

force()


                #STRING MANIPULATION

#02.2.1 Characters

word = input('Write the word you want to modify: ')
lenght = len(word)

print(word[0 : 3] + '...' + word[lenght-3 : lenght])

#02.2.2 Telephone Number

number = input('Write your telephone number: ')

if len(number)==10:
    print('Your telephone number is: ' + '(' + number[0:3] + ')' + ' ' + number[3:6] + '-' + number[6:len(number)])
else: 
    print('Enter a valid phone number!')


#02.2.3 Alignment

a = int(input('Insert the first number: '))
b = int(input('Insert the second number: '))

sum = a+b
diff = a-b
product = a*b
avg = float((a+b)/2) 
dist = abs(a-b)
maxx = max(a,b)
minn = min(a, b)

operation = ['Sum: ', 'Difference: ', 'Product: ', 'Average: ', 'Distance', 'Maximum', 'Minimum']
values = [sum, diff, product, avg, dist, maxx, minn]

for i in range(0, 7):
    print(' ')
    print(f"{operation[i] : <15} {values[i]}")


#02.2.4 Emoji

fields = ['Position in ranking', 'Unicode number', 'Unicode name', 'Emoji']
position = [1,2,3]
number = ['U+1F602','U+2764', 'U+1F601']
name = ['FwToJ', 'BHS', 'GFwSE']
emoji = ['laughing', 'red heart', 'smile']

types = ['Face with tears of joy: ','Heart symbol: ','Smiling face: ']

print(f"{'Position in ranking' : >50}{'Unicode number' : >25}{'Unicode name' : >25}{'Emoji' : >15}")

for i in range(0, 3):
    print('')
    print(f"{types[i]: >25}{position[i] : >15}{number[i] : >30}{name[i] : >25}{emoji[i] : >20}")



#02.2.5 Registrations

freshman = ['s312576','s311566']
sorted_list = sorted(freshman)

print('Ascending order freshmen:   \n' + ' \n'.join(sorted_list))