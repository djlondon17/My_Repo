my_list = [1, 2, "up", "down", "left"]
# print(my_list)
# print(my_list[0])
# print(my_list[-1])
del my_list[0] # deletes the object in the element position
print(my_list)
my_list.remove(2) # removes all matching objects in the list
print(my_list)
my_list.append(input("What is missing from this list? ")) # adds element to end of list
print(my_list)