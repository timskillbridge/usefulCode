import pytest
import functools

list1 = [1,2,54,66,7,3,2,76,8,4,3,4,55,2,7,335,9]
list2 = [1,2,3,4,5,6,7,8,9,0]
list3 = []

def alsoLen(test_list):
    if not isinstance(test_list,list): return False
    try:
        testVal =  test_list.index(test_list[-1])+1
        '''testVal = testVal'''
    except:
        return 0
    
    return int(f"{test_list.index(test_list[-1])+1}")

print(alsoLen(list1))
print(alsoLen(list2))
print(alsoLen(list3))
print(len(list3))

just_a_string = "abcdefghijklmnopqrstuvwxyz"

for x, y in enumerate(just_a_string):
    print(f"index {x} holds a value of {y}, which is {ord(y)} in ASCII")

for x in enumerate(just_a_string):
    print (x[1])

name_list = ["asdf","sdfg"]

name_list.insert(0,"asdaaaaf")
name_list.remove(name_list[len(name_list)-1])

print(name_list)

def checkDictionary(dictionary:dict, type1,type2):
        keyCheck = set(map(type,dictionary.keys())) == {type1}
        valCheck = set(map(type,dictionary.values())) == {type2}
        if valCheck and keyCheck:
            return True
        else:
            return False
        
list4 = [1,2,3,4,5]
new_list4 = list(map(lambda x: x *x,list4))
print(new_list4)

#sort dictionary by key using lamda

people = [
     {          
        'name':"alice",
        'age': 40,
        'job:':"secretary",
     },
     {          
        'name':"bob",
        'age': 51,
        'job:':"hair stylist",
     },
     {          
        'name':"carol",
        'age': 35,
        'job:':"coach",
     }
]

print(sorted(people,key = lambda person : person['age'], reverse=True))

list5 = ["a","b","c","d","e","F","G","h","i","J","k","l"]
list6 = [1,2,3,4,5,6,7,8,9]

dict_list = dict(zip(list5,list6*2))  # multiplying a list by a number ensures it's longer and won't be the shortest in the zip; Zip zips the shorest.
zip_list = list(zip(list5,list6*99))
print(dict_list)
#unzip stuff
other_list, other_other_list = zip(*zip_list)

print(f"{other_list} and {other_other_list}")

my_num = 5

print(type(my_num))
print(type(my_num/1))

my_num2 = 5
my_num3 = 7

my_list = [1,2,3]
my_other_list = [4,5,6]
my_third_list = [[i for x in range(5)] for i in range(3)]

print(my_third_list)

print(type(my_list))
print(type(my_list) == list)

x = 1.1

print(not isinstance(x,(float,int)))


#reduce and
my_list = [1,2,3,4,5,6,7,8,9,10]
sum = functools.reduce(lambda agg, item : agg + item, my_list)
print(sum)