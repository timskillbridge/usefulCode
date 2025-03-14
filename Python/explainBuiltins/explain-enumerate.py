

# Enumerate runs through a list's indicies, eliminating the need for a range() in a loop
#when offered a single variable in a for loop, in this case x, it returns a tuple which can be manipulated accordingly.

just_a_string = "abcdefghijklmnopqrstuvwxyz"

for x in enumerate(just_a_string):
    print (x[1])

#returns each character in the string, 'just_a_string' because x is a touple with two indecies,
#the first is the index number in the touple and the second is the value

# The same could be done with a standard for loop:

print(f"\n")

for x in range(len(just_a_string)-1):
    print (just_a_string[x])

# Enumerate also allows two arguments, one for each item in the tuple.

just_a_backwards_string = just_a_string[::-1]

for x, y in enumerate(just_a_backwards_string):
    print(f"index {x} holds a value of {y}, which is {ord(y)} in ASCII")

# This makes it very easy to access both the index and value
# You can also use the index numbers across two lists/strings if the lengths match

for x, y in enumerate(just_a_string):
    print(f"just a string index {x}: '{y}' and just a backwards string value at index {x}: '{just_a_backwards_string[x]}'")

