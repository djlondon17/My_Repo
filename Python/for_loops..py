my_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Gundam"]
abc = ["A", "B", "C", "D", "E", "F", "G"]

'''
count = 0
while count < len(my_list):
    print(my_list[count])
    count += 1
'''

for i, j in zip(abc, my_list):
    print(i + " is for " + j)