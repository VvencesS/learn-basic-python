# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

info = ["Duc", "Soan", 21]
formatString = "Hello"
programmingLanguage = ["Java", "C sharp", "Python"]

print("%s, My name is %s %s, %d years old. I'm learning %s"
      % (formatString, info[0], info[1], info[2], programmingLanguage))