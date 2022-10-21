var1 = "This "
var2 = "is "
var3 = "a "
var4 = "test!"
print(var1 + var2 + var3 + var4)

my_tuple = ("This ", "is ", "a ", "test!")

string = ""
for i in my_tuple:
    string = string + i
print(string)

other_tuple = ("This", "is", "a", "test!")
print(" ".join(other_tuple))
print("-".join(other_tuple))
print("".join(other_tuple))