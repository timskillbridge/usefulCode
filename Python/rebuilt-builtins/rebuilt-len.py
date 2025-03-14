
def rebuiltLen(test_list):
    if not isinstance(test_list,list): return False
    try:
        testVal =  test_list.index(test_list[-1])+1
        '''testVal = testVal'''
    except:
        return 0
    
    return int(f"{test_list.index(test_list[-1])+1}")

print(rebuiltLen([1,2,3,4,5,6]) == 6)

print(rebuiltLen([]) == 0)

print(rebuiltLen("string") == False)