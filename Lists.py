# Add numbers and strings to the correct lists using the "append" list method.
# Fill in the variable second_name with the second name in the names list, using the brackets operator [].

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

print("Numbers list: ", end="")
print(numbers)
print("Strings list: ",  end="")
print(strings)
print("The second name on the names list: " + names[1])