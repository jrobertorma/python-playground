## We can use input() to interact with the user using the CLI, 'a la' 'C', Py doesn't use semicolons to end sentences
stringNumber = input('Gib number :3 ')

## input always returns a string, so if you want an int you should convert the returned value first
intNumber = int(stringNumber)

## Py uses implicit types BTW

## Conditional statements have this syntax
if intNumber > 15 :
    ## notice the indentation, it works as the old '{ }' (curly braces) of 'C'
    print('bigger than 15')
## We can call an if inmediately within an else block with 'elif'
elif intNumber > 10 :
    print('bigger than 10 smaller than 15')
else : 
    print('smaller than 10 (and than 15 lol)')

## Output throug console
print('number was:', intNumber)