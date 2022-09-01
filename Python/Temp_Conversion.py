'''
temp = float(input("What is the tempature?: "))
indicator = input("F or C: ")

if indicator == "C":
    f_temp = (temp * 1.8) + 32
    print(f"Temp in Celcius: {temp}")
    print(f"Temp in Fahrenheit: {f_temp}")
elif indicator == "F":
    c_temp = (temp - 32) / 1.8
    print(f"Temp in Fahrenheit: {temp}")
    print(f"Temp in Celcius: {c_temp}")
'''

tempature = float(input("What is the tempature?: "))
indicator = input("F or C: ")

if indicator == "F":
    C_tempature = (tempature - 32) / 1.8
    print(tempature, C_tempature)