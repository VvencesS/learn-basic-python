s = "Hey there! what should this string be?"

# String length
print("Length of s: %d" % len(s))

# First occurrence of "a" on s string
print("The first occurrence of the letter 'a': %d" % s.index("a"))

# Number of occurrences of "e"
print("'e' occurs  %d times" % s.count("e"))

# Slicing the string into bits
print("The first five characters are: '%s'" % s[:5])
print("The next five charcters are: '%s'" % s[5:10])
print("The thirteen character is: '%s'" % s[12])
print("The characters with odd index are: '%s'" % s[1::2])
print("The last five characters are: '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Hey"):
    print("String starts with 'Hey'")

# Check how a string ends
if s.endswith("be?"):
    print("String ends with 'be?'")

# Split the string  into  separate strings, each containing only a word
print("Split the words of the string: %s" % s.split(" "))
