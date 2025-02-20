def compare_dict_to_class(testDict,testClass):
    keys = {}
    for x,y in enumerate([key for key in testClass.__dict__.keys()]):
        keys[y[1::]] = x
    # print(f"{type(keys.keys())} : {keys}")
    # print(f"{type(testDict)} : {testDict}")
    return keys.keys() == testDict.keys()