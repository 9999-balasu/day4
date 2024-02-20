

print("Today Topics")

print("Rules for declaring variables")


#A variable name must start with a letter or the underscore character.
#A variable name cannot start with a number.
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)
print('Mutability vs Immutability')

#Mutability vs Immutability
#In programming, you have an immutable object if you can’t change the object’s state after you’ve created it.
# In contrast, a mutable object allows you to modify its internal state after creation. 
#In short, whether you’re able to change an object’s state or contained data is what defines if that object is mutable or immutable.')
print('Immutable Data types in Python')
print(' Numeric')
print('string')
print(' Tuple')

print('Mutable Data types in Python')
print('List') 
print('Dictionary') 
print('Set') 

#Python List Methods
#Python has many useful list methods that make it really easy to work with lists.

#Method	Description
#append()	Adds an item to the end of the list
#extend()	Adds items of lists and other iterables to the end of the list
#insert()	Inserts an item at the specified index
#remove()	Removes item present at the given index
#pop()	Returns and removes item present at the given index
#clear()	Removes all items from the list
#index()	Returns the index of the first matched item
#count()	Returns the count of the specified item in the list
#sort()	Sorts the list in ascending/descending order

ages=[19,28,34]
print(ages)

languages=['python','C languge','c++','javascript','React.js']
print(languages)
print(languages[0])
print(languages[1])
print(languages[2])
print(languages[3])
print(languages[4])

languages.append('java')
print(languages)