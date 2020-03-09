number = 10
firstArray = []
secondArray = [1, 2, 3]

if number > 15:
    print("Number greater than 15!")
else:
    print("Number is not greater than 15!")

if firstArray:
    print("The array is not empty!")
else:
    print("Empty array!")

if len(secondArray) == 3:
    print("Length of secondArray: %d" % len(secondArray))

if len(firstArray) + len(secondArray) == 3:
    print("Length of two arrays: 3")

firstArray.append(1)
if firstArray and secondArray[0] == 1:
    print("Two arrays have '1' element")