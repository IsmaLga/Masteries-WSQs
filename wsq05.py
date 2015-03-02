f = int(input("What's the temperature in farenheit degrees?"))
c = 5*(f-32)/9

print ("A temperature of", f,"degrees Farenheit is ", c, "centigrades")
if (c > 100):
    print ("Water does boil at this temperature (under typical conditions).")
else:
    print ("Water does not boil at this temperature (under typical conditions).")
