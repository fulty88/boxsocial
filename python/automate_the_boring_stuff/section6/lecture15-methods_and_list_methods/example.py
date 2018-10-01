# Index method
spam = ['Hello', 'Hi', 'Howdy', 'Heyas']
print('My list:')
print(spam)
print('Heyas is located in index: ' + str(spam.index('Heyas')))

# Append method
print('Adding "Bonjour" to the end of the list')
spam.append('Bonjour')
print(spam)

# Insert method
print ('Inserting "Hola" into index 1 of the list')
spam.insert(1, 'Hola')
print(spam)

# Remove method
print('Removing "Hi" from the list')
spam.remove('Hi')
print(spam)
