
# isinstance checks to see if a provided variable is of a specified type
# the difference between thsi and 'type()', is isinstance checks for
# sub-classes as well as main classes.
# this is useful in error catching
# to check multiple types, encapsulate them in parenthesis separated by a comma (type1,type2,etc...)

# provide a variable
x = 1.1 #simple float

#execute using print to see results
print(isinstance(x,(float,int)))
# returns True because 1.1 is type float

print(not isinstance(x,(float)))
# returns False because 1.1 is a float; we specified 'not' so its looking for not a float

x = [1,2,3,4,5]
print(isinstance(x,(list,set)))
# returns True, x is a list or a set, list in this case.