# Create a string, an integer, and a floating point number.

myString = "hello world"
myFloat = float(10)
myInt = int(20)

if myString == "hello world":
    print("String: %s" % myString)
if isinstance(myFloat, float) and myFloat == 10.0:
    print("Float: %f" % myFloat)
if isinstance(myInt, int) and myInt == 20:
    print("Int: %d" % myInt)

