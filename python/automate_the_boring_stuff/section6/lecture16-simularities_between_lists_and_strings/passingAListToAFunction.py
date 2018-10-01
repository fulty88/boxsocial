def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# The spam list reference is copied to the parameter "someParameter".
