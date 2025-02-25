
import time
import random
import sys
import subprocess



def text_rain(text):
    fill_list = [" " for x in text]
    text_order = [int(x) for x in range(len(text))]
    for x in range(100):
        r1 = random.randint(0,len(text)-1)
        r2 = random.randint(0,len(text)-1)
        hold = text_order[r1]
        text_order[r1] = text_order[r2]
        text_order[r2] = hold
    # print(text_order)
    for x in range(len(fill_list)):
        time.sleep(.1)
        fill_list[text_order[x]] = text[text_order[x]]
        # print(f" {"".join(fill_list)}  fill_order:{x} is {fill_list[text_order[x]]} in space {x} text_order: {text_order[x]} {text[text_order[x]]}")
        print(" " + "".join(fill_list),end='\r')
        

    print(f" {"".join(fill_list)}")

# text_rain(" The random group of letters in this sentence might not print correctly")


if __name__ == "__main__":
    arg = sys.argv[1]
    text_rain(arg)