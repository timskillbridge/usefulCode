import time #<----For the pausing between prints
import subprocess  #<---- for Screen clearing

subprocess.run('clear',shell=True) # <------Clears the terminal

string = [f" {x}" for x in "Typing out in the console, one character at a time".split(" ")]  #<-- fills a list. Each item is proceeded by a " "

for a,b in enumerate(string):   
    for c,d in enumerate(b):
        print(f'{b[0:c]}', end='\r')  # Print and overwrite the same line  
        time.sleep(.1)  # Pause for 1 second
    print(b[1:]) #<--- cuts off the space from the whole word so the final print of the full word doesn't stick ouu.

 # strLength = []
# for x in range(len(string)):
#     strLength.append(x)
# # print(strLength)
# string1 = " Single Line String"
# string2 = " multi"
# string3 = " line"
# string4 = " strings"


# for i,j in enumerate(string1): 
#     print(f'{string1[0:i]}', end='\r')  # Print and overwrite the same line 
#     time.sleep(.2)  # Pause for 1 second 
# print(string1)
# for i,j in enumerate(string2): 
#     print(f'{string2[0:i]}', end='\r')  # Print and overwrite the same line 
#     time.sleep(.2)  # Pause for 1 second 
# print(string2)
# for i,j in enumerate(string3): 
#     print(f'{string3[0:i]}', end='\r')  # Print and overwrite the same line 
#     time.sleep(.2)  # Pause for 1 second
# print(string3)
# for i,j in enumerate(string4): 
#     print(f'{string4[0:i]}', end='\r')  # Print and overwrite the same line 
#     time.sleep(.2)  # Pause for 1 second
# print(string4)


# print(string2)  # Print "Done!" after the loop 

