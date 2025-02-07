
#create some random lists
list5 = ["a","b","c","d","e","F","G","h","i","J","k","l"]
list6 = [1,2,3,4,5,6,7,8,9]


#create a dicationary using the ilsts via dictionary casting and zip
dict_list = dict(zip(list5,list6*2))  # multiplying a list by a number ensures it's longer and won't be the shortest in the zip; Zip zips the shorest.

#create list using zip and two lists, extending out the shorter list to ensure the longer is zipped in entirety.
#zip will only sip up to the length of the shortest list

zip_list = list(zip(list5,list6*99))
print(dict_list)

#unzip stuff
# unzip from a zipped list into two new lists
other_list, other_other_list = zip(*zip_list)
print(f"{other_list} and {other_other_list}")
