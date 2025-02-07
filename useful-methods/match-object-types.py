

#takes a dictionary and verifies all its keys are the same type and all the values are the same type
#this can help eliminate errors when using different custom dictionary classes

def checkDictionary(dictionary:dict, type1,type2):
        keyCheck = set(map(type,dictionary.keys())) == {type1}
        valCheck = set(map(type,dictionary.values())) == {type2}
        if valCheck and keyCheck:
            return True
        else:
            return False
        
# The code defines two sets, one for keys in the dictionary and one for values
# Each set uses a map to apply the method 'Type()' against all keys or values
# Each set is compared to a set with a single entry of the type provided in the parameter (argument at run time)
# If the created sets match the provided value types, the fucntion returns True
# Otherwise False is returned

