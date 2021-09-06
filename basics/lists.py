# A list is a collection of items, that behave like 'variables'
# we declare a list with [], every item is separated by a comma (,)
elBoom = ['Rulfo', 'Onetti', 'Cortázar', 'Márquez']

# We can access every item with an index, likewise strings
print(elBoom[0]) #'Rulfo'

# We can store every Python object in a list, including other lists
sqareMatrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(sqareMatrix[0][1]) # 2

# Definite lopps and lists get along pretty well
for author in elBoom :
    print(author)

# String are inmutable, lists are mutable
lotto = [2,14,26]
lotto[1] = 15
print(lotto) # 2,15,16

# The len() function also returns the lenght of a list
print(len(elBoom)) # 4

# The range function returns a sequence of integers (not a list, at least not in py 3.9.6) 
# that start at 0 and end at the parameter without including it
indexes = range(4)
for i in indexes :
    print(i)
# [0,1,2,3]

# We can use the range() function to create an 'Index loop'
for i in indexes :
    author = elBoom[i]
    print('Boom author:',author)

# We can concatenate lists with +
modernistas = ['Darío', 'Lugones', 'Martí', 'Díaz Mirón']
allStars = modernistas + elBoom
print (allStars) #['Darío', 'Lugones', 'Martí', 'Díaz Mirón', 'Rulfo', 'Onetti', 'Cortázar', 'Márquez']

# We can split lists like with stringsm notice the second index means 'up to but not including it'
print(allStars[2:5]) #['Martí', 'Díaz Mirón', 'Rulfo']

# We can add new elements at the end of a list with append()
allStars.append('Paz')
print(allStars) # ['Darío', 'Lugones', 'Martí', 'Díaz Mirón', 'Rulfo', 'Onetti', 'Cortázar', 'Márquez', 'Paz']

# We also can look for 'something' within a list with the 'in' keyword, it will return true or false
print('Alamán' in allStars) # false
print('Lugones' in allStars) # true

# The sort() method orders the list, strings will be order alphabetically by default, this method 'mutates' the original list
allStars.sort()
print(allStars) # ['Cortázar', 'Darío', 'Díaz Mirón', 'Lugones', 'Martí', 'Márquez', 'Onetti', 'Paz', 'Rulfo']

# Lists are very useful to handle numbers (e.g. to use for linear algebra and matrices)
nums = [0,1,1,2,3,5,8,13,21,34,55,89,144]

print(len(nums)) # 13, the list's length
print(max(nums)) # 144, the highest number
print(min(nums)) # 0, the shortest number
print(sum(nums)) # 376, the sum of all the numbers
print(sum(nums)/len(nums)) # 28.92, we can get the average by dividing the sum of all the numbers with the number of numbers (lol)