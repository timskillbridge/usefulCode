

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
print(sorted(people,key = lambda person : person['name']))