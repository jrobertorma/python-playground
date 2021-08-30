# Python also has the function concept, i.e. "Reusable pieces of code"
# we can use the 'def' keyword that stands for 'define function'

# Function declaration
def multipleGreetings(name,times) :
    # Python can implement 'while' loops like this
    n = 0
    while n < times :
        print("Hello",name)
        n= n + 1
    print("Loop end n:",n)

# Function invoking, notice the arguments and how you catch them in the function declaration
print(multipleGreetings("Jr",2))

# There are also the 'definite loops'
def multipleForGreetings(names) :
    for name in names :
        print("Hello",name)
    print("For end")

beatles = ['John','Paul','George','Ringo']
print(multipleForGreetings(beatles))