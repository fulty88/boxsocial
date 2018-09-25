# This program says hello and asks for my name and age.

print('Hello World')
print('What is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?') # ask for their age
myAge = input()
print('My age is: ' + myAge)
print('Nice. In 1 year you will be ' + str(int(myAge) + 1) + ' years old')
