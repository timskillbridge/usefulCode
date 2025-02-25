
import sys, subprocess, time, termios, tty
import readline
from text_rain import text_rain  #  <--- importing from another file to pass to menu in argument

def clear_screen():
    subprocess.run('clear',shell=True)

oldval = [27906, 5, 1215, 35387, 15, 15, [b'\x03', b'\x1c', b'\x7f', b'\x15', b'\x04', b'\x00', b'\x01', b'\x00', b'\x11', b'\x13', b'\x1a', b'\xff', b'\x12', b'\x0f', b'\x17', b'\x16', b'\xff', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00']]
#    ^
#    | - > this is the value of termios.tcgetattr(sys.stdin).  It's there in case the program crashes and jacks up our terminal we can restore it to normal values upon re-running the program.


def restore_settings():
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldval)
    
def navigate_menu(list_options:list, list_menu_methods:list=[]):
    clear_screen()
    nav = 0    #  <--- This is how we navigate the system; it keeps track of what menu item is selected.  0 is the bottom option which is QUIT
    
    print("\n")    #  <--- I just like having a buffer from the top of the screen

    for x in range(len(list_options)-1,-1,-1):    #  <--- print the initial menu from the list of arguments, then print QUIT option and append it to the options for future use
        print(list_options[x])
    print(f"\u001b[33m-----QUIT\u001b[0m")
    list_options.insert(0,"QUIT")
    
    running = True
    while running:    #  <--- Lets run this loop to start the program.
        tty.setraw(sys.stdin)    #  <--- get raw keyboard iput
        char = sys.stdin.read(1)    #  <--- grab the first part of the raw input
        escape_sequence = ''    #  <--- define an escape sequence for later
        if ord(char) == 27:    #  <--- keyboard input was an esape sequence, we'll use that later to check if it's an arroow key.
            escape_sequence = '\x1b' + sys.stdin.read(2)
        restore_settings()
        if ord(char) == 3:    #  <--- CTRL + C, user is trying to force quit so we allow it
            restore_settings()
            running = False    #  <--- let the user force quit
        if char in ['\n','\r']:    #  <--- enter key was pressed, select an option
            if nav == 0:    #  <--- user chose to quit
                restore_settings()
                clear_screen()
                running = False
            else:    #  <--- uswer is choosing an option from one in the list
                restore_settings()
                clear_screen()
                if "(" in list_menu_methods[nav-1]:

                        passed_method = list_menu_methods[nav-1][0:list_menu_methods[nav-1].index("(")]
                        tempname = list_menu_methods[nav-1]
                        checkargs = tempname[tempname.index("(")+1:tempname.index(")")]
                        globals()[passed_method](checkargs)    #  <--- run the selected menu option
                else:
                        passed_method = list_menu_methods[nav-1]
                        globals()[passed_method]()
                x = input("press any key to return")    #  <--- give the user a break in case they want to see the output from the prior run menu option
                clear_screen()
                nav = 0
                
                clear_screen()
                print("\n")    #  <--- re-create that buffer from the initial menu print, then print the initial menu again
                for x in range(len(list_options)-1,0,-1):
                    print(list_options[x])
                print(f"\u001b[33m-----QUIT\u001b[0m")

        else:    #  <--- something that wasn't the enter key was hit in the raw input gathered earlier
            if escape_sequence == '\x1b[A':    #  <--- it was the up arrow key, so we adjust the displayed menu
                if 0 <= nav < len(list_options)-1:
                    
                    nav +=1    #  <--- tell the prgram we're moving our selection up
                    sys.stdout.write(f'\x1b[1A')    #  <--- move the print-line up 1 line, now we're off the bottom line where you normally type
                
                    sys.stdout.write(f'\x1b[{nav}A')    #  <--- move up the number of lines we need to get to the new selection
                    sys.stdout.write('\x1b[2K\r\x1b[K')    #  <--- clear that line of any prior data
                    sys.stdout.flush()    #  <--- clear prior written data from memory

                    
                    print(f"\u001b[33m-----{list_options[nav]}\u001b[0m ")    #  <--- print the newly selected line in yellow, offset by some -----s to make it stand out
                    for x in range(nav):    #  <--- clear and re-print the options below in regular fashion
                        sys.stdout.write("\u001b[1000D")
                        sys.stdout.write('\x1b[2K\r\x1b[K')
                        print(f"\u001b[0m{list_options[nav-1-x]}")

                else:    #  <--- we're at the top of the options, move the selction cursur and reset nav to the bottom
                    nav = 0
                    clear_screen()
                    print("\n")
                    for x in range(len(list_options)-1,0,-1):
                        print(list_options[x])
                    print(f"\u001b[33m-----QUIT\u001b[0m")


            if escape_sequence == '\x1b[B':    #  <--- user hit the down arrow
                
                if 0 < nav <= len(list_options):    #  <--- check if we're above line 1 and adjust the nav and re-print the menu with the correct selected item
                    nav -= 1
                    clear_screen()
                    print('\n')

                    for x in range(len(list_options)-1,-1,-1):
                        if x != nav:
                            print(f"{list_options[x]}")
                        else:
                            print(f"\u001b[33m-----{list_options[nav]}\u001b[0m ")

                else:    #  <--- we're at the bottom, re-do the menu to have the top selected
                    nav = len(list_options)-1
                    clear_screen()
                    print('\n')
                    print(f"\u001b[33m-----{list_options[nav]}\u001b[0m ")
                    for x in range(len(list_options)-2,-1,-1):
                        print(list_options[x])
    
    clear_screen()



def option1():
    # clear_screen()
    print("Called option1")
    
def menu_program_2():
    for x in range(30):
        time.sleep(.2)
        print(x)

# navigate_menu(['First Option', 'Second option', 'Third option'],["option1","menu_program_2","text_rain(abcdefghijklmnopqrstuvwzyyyyyy ...yes, that ws intentional - z)"])

if __name__ == "__main__":
    if 0 < len(sys.argv) < 3:
        print(f"""This method takes two arguments, both are lists.
            1. List of menu options
            2. List of names of functions to be called for the corresponding menu options.
            If the functions contain arguments, type them in as text in the regular format""")
        sys.exit(1)
    try:
        if len(sys.argv[1]) >0:
            list_of_options = sys.argv[1][1:len(sys.argv[1])-1].split(",")
            
        if len(sys.argv[2]) >0:
            list_menu_functions = sys.argv[2][1:len(sys.argv[2])-1].split(",")

    except:
        print("lists provided were not valid")
        sys.exit[1]
    navigate_menu(list_of_options,list_menu_functions)


