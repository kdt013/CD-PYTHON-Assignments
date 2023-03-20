num1 = 42 #number/var declaration
num2 = 2.3 #decimal/var declaration
boolean = True #boolean
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #tuples
fruit = ('blueberry', 'strawberry', 'banana') #list
print(type(fruit)) #print fruit list
print(pizza_toppings[1]) #print index 1 of pizza_toppings list
pizza_toppings.append('Mushrooms') #add value to pizza_toppings list
print(person['name']) #print the name from list person
person['name'] = 'George' #change name is George
person['eye_color'] = 'blue' #add eye color to person
print(fruit[2]) #print index 2 of list fruit

if num1 > 45: #conditional if/else
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: #conditional if/else
    print("It's a short word!")
elif len(string) > 15: #else if
    print("It's a long word!")
else: #else
    print("Just right!")

for x in range(5): #for loop
    print(x)
for x in range(2,5): #for loop
    print(x)
for x in range(2,10,3): #for loop
    print(x)
x = 0
while(x < 5): #while loop
    print(x)
    x += 1

pizza_toppings.pop() #remove last value from pizza_toppings list
pizza_toppings.pop(1) #remove index 1 from pizza_toppings list

print(person) #print person tuple
person.pop('eye_color') #remove eye color from person tuple
print(person) #print person tuple

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue                        #for loop with nested if statements
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():    #define function
    for num in range(10):       #for loop
        print('Hello')          #print statement

print_hello_ten_times()         #print function above

def print_hello_x_times(x):     #new function 
    for num in range(x):        #for loop
        print('Hello')          #print statement

print_hello_x_times(4)         #print above function 4 times

def print_hello_x_or_ten_times(x = 10):     #function that takes a parameter x=10
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()    #print function
print_hello_x_or_ten_times(4)   #print function 4 times


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)