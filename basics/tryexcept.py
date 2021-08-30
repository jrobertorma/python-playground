# If there is a piece of code than can blow up the program we can use the try/except keywords
stringInput = input('Gib number please :3 ')

# Converting a text string into an int usually would stop the program
# if we use the try/except structure we can prevent that and define a 'default'
# block of code to handle those situations 
try :
    convertedInput = int(stringInput) 
except :
    convertedInput = -1

if convertedInput > 0 : 
    print('You entered a number! :) - ',convertedInput)
else :
    print('Not a number :( - ', stringInput)
