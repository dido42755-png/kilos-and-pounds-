weight = input("enter your weight  ")
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted = int(weight) * 0.45
    print("you are " + str(converted) + " kilos")
else:
    converted = int(weight) / 0.45
    print("you are " + str(converted) + " pounds")