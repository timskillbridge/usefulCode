import time
import random
import sys
import subprocess


def grid3x3():
    subprocess.run('clear',shell=True)

    list_of_nums = [0,1,2,3,4,5,6,7,8,9]
    fill_list = ["x"]*(len(list_of_nums))
    # print(len(fill_list))

    for x in range(50):
        r1 = random.randint(0,9)
        r2 = random.randint(0,9)
        hold = list_of_nums[r1]
        list_of_nums[r1] = list_of_nums[r2]
        list_of_nums[r2] = hold

    # print(list_of_nums)

    print(f"   [ {fill_list[0]} ] [ {fill_list[1]} ] [ {fill_list[2]} ]\n   [ {fill_list[3]} ] [ {fill_list[4]} ] [ {fill_list[5]} ]\n   [ {fill_list[6]} ] [ {fill_list[7]} ] [ {fill_list[8]} ]\n")

    for x,y in enumerate(list_of_nums):
        # print(f"{x} {y}\n")
        fill_list[y] = list_of_nums[y]
        time.sleep(.3)
        
        # [7, 2, 0, 9, 4, 3, 8, 6, 5, 1]
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        if y < 3:
            
            sys.stdout.write('\u001b[4A')  # Move up 3 lines
            sys.stdout.write('\x1b[2K\r\x1b[K')  # Clear the line
            sys.stdout.flush()
            print(f"   [ {fill_list[0]} ] [ {fill_list[1]} ] [ {fill_list[2]} ]") #1 fill_list[x] = {fill_list[x]}, came from list_of_nums[x] {list_of_nums[x]}, y={y}, being tested")
        elif 3 <= y < 6:
            sys.stdout.write('\u001b[3A')  # Move up 2 lines
            sys.stdout.write('\x1b[2K\r\x1b[K')  # Clear the line
            sys.stdout.flush()
            print(f"   [ {fill_list[3]} ] [ {fill_list[4]} ] [ {fill_list[5]} ]") #2 fill_list[x] = {fill_list[x]}, came from list_of_nums[x] {list_of_nums[x]}, y={y}, being tested")
        elif 6 <= y < 10:
            sys.stdout.write('\u001b[2A')  # Move up 1 line
            sys.stdout.write('\x1b[2K\r\x1b[K')  # Clear the line
            sys.stdout.flush()
            print(f"   [ {fill_list[6]} ] [ {fill_list[7]} ] [ {fill_list[8]} ]") #3 fill_list[x] = {fill_list[x]}, came from list_of_nums[x] {list_of_nums[x]}, y={y}, being tested")

        # Move the cursor back down to the next row
        if y < 3:
            sys.stdout.write('\u001b[3B')
        elif 3 <= y < 6:
            sys.stdout.write('\u001b[2B')
        elif 6 <= y < 10:
            sys.stdout.write('\u001b[1B')

        sys.stdout.flush()
# random_populate()

if __name__ == "__main__":
    rand_populate()