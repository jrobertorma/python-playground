# Python makes file reading a very simple task
# first we need to create a 'file handle', wich is a kind of link to the file
# not the file itself, the open() function returns a file handle
# open('filename','mode')
# filename must be a string, mode must be 'r' for reading, 'w' for writing

handle = open('../resources/mail-log.txt','r')
for line in handle :
    print(line.rstrip()) # every line has a \n at the end, that counts as whitespace, we can remove them with rstrip()

# we can omit lines that we don't need
for line in handle :
    line = line.rstrip()
    # I don't want to see empty lines
    if not line.startswith('20') : 
        continue
    print(line)

# Also we can look for a substring to decide if the program prints the line or not
for line in handle :
    line = line.rstrip()
    # I only want the lines with @, so I skip the loop when the line doesn't contain the character
    if not '@' in line : 
        continue
    print(line)