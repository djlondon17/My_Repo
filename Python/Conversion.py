question = input("How would you like to convert:\n(1). From Fahrenheit to Celsius\n(2). From Celsius to Fahrenheit\nYour Choice: ")

if question == "1":
    fahrenheit = float(input("What is the tempature in Fahrenheit? "))
    celsius = (fahrenheit - 32) / 1.8
    print(str(fahrenheit) + " degrees fahrenheit converts to " + str(round(celsius, 1)) + " degrees celsius")
elif question == "2":
    celsius = float(input("What is the tempature in Celsius? "))
    fahrenheit = (celsius * 1.8) + 32
    print(str(celsius) + " degrees celsius converts to " + str(round(fahrenheit, 1)) + " degrees fahrenheit")
else:
    print("Sorry, I didn't understand. Good bye!")