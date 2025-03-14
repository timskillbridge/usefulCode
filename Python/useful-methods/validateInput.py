'''Use to determine if one or more arguments is of a certain type

if validateInput(arglist,type) == False:
    pass
else:
    whatever
'''
def validateInput(arglist, type):
        if type == int:
            try:
                for x,y in enumerate(arglist):
                    y = int(y)
            except:
                return False
            return arglist
        elif type == str:
            try:
                for x,y in enumerate(arglist):
                    y = str(y)
            except:
                return False
            return arglist
        else:
            return False