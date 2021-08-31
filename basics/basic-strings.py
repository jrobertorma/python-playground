# A string is a sequence of characters, we use "" to define them
# Strings have indexes starting at 0, we can't access unexistent indexes
# the len() function returns the lenght of a string

fruit = '¡Plátanooooo!'
index = 0

while index < len(fruit) :
    letter = fruit[index]
    print("Index:",index,"Letter:",letter)
    index = index + 1

# We can 'extract' substrings from a string using its indexes
fruit = '¡Manzanaaaaaaaa!'
halfFruit = fruit[0:5]
print(halfFruit) #!Manz
otherHalf = fruit[5:8] #ana
print(otherHalf)

# When we left the first or last index empty, Python takes it as the start or end of the string
print(fruit[:5]) #!Manz
print(fruit[5:]) #anaaaaaaaa!

# We can use the keyword 'in' to look for a substring within a string, it returns 'true' or 'false'
fruit = '¡Manzanaaaaaaaa!'
print ('an' in fruit) # True
print ('sa' in fruit) # False

# Strings have several built in functions that can be very useful
# The find() method looks for a substring and returns the position if there are coincidences, it there aren't returns -1
fruit = '¡Papayaaaaaaaa!'
pos = fruit.find('ya')
print (pos) # 5

# The upper() and lower() methods return a new string with the string in lower/upper case
greet = "ThIs is A GReeTinG"
lowerGreet = greet.lower()
print(lowerGreet) # this is a greeting
upperGreet = greet.upper()
print(upperGreet) # THIS IS A GREETING

# The replace() method search and replaces a substring within a string
greet = "Hello Bob"
newGreet = greet.replace('Bob','Joe')
print(greet) # Hello Bob
print(newGreet) # Hello Joe

# The lstrip(), rstrip() and strip() methods remove the white space from the start, end or both sides of a string respectively
word = "   Yoyoyo, I'm JRMA   "
print(word) #'   Yoyoyo, I'm JRMA   '
print(word.lstrip()) # 'Yoyoyo, I'm JRMA   '
print(word.rstrip()) # '   Yoyoyo, I'm JRMA'
print(word.strip()) # 'Yoyoyo, I'm JRMA'

# The startswith() method looks for a provided substring at the start of a string
line = 'Have a nice day!'
print (line.startswith('Have')) # True
print(line.startswith('have')) # False
print(line.startswith('ave')) # False