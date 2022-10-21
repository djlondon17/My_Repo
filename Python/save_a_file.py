'''
file = open("saved_file.txt", 'w')
file.write("This is a saved file.")
file.close()

'w' erases the file and writes over it
'a' appends the file and adds to it
'''

with open('saved_file.txt', 'a') as file:
    file.write("And this is yet another line.\n")