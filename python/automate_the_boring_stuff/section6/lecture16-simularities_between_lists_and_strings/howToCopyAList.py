import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
print(cheese)
cheese[1] = 'Cheese'
print(cheese)
print(spam)
