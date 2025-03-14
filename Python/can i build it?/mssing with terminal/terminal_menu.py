
                                                        ###################################
                                                        ##        NEEDED IMPORTS         ##
                                                        ###################################
import sys, subprocess, termios, tty, readline, importlib, os
#sys        -needed to access the sys.stdout.write and associated functions
#termios    -needed to restore terminal functionality from just receiving raw input and displaying raw output
#tty        -needed to solicit raw input
#readline   -needed to prevent arrow key input while getting user input via input()
#importlib  -needed to dynamically import functions contained in external modules using veriable names...pretty cool, saves on importing

                                                        ###################################
                                                        ##        HELPER METHODS         ##
                                                        ###################################

def clear_screen():
    subprocess.run('clear',shell=True)

def restore_settings():
    oldval = oldval = [27906, 5, 1215, 35387, 15, 15, [b'\x03', b'\x1c', b'\x7f', b'\x15', b'\x04', b'\x00', b'\x01', b'\x00', b'\x11', b'\x13', b'\x1a', b'\xff', b'\x12', b'\x0f', b'\x17', b'\x16', b'\xff', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00']]
    #    ^
#    | - > this is the value of termios.tcgetattr(sys.stdin).  It's there in case the program crashes and jacks up our terminal we can restore it to normal values upon re-running the program.
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldval)


                                                        ###################################
                                                        ##        MAIN PROGRAM           ##
                                                        ###################################

def navigate_menu(list_options:list, list_menu_methods:list=[]):
###################################
##        PREP THE PROGRAM       ##
###################################

    clear_screen()
    nav = 0                                             # - navigate using this variable, 0 is the default value and equal to "QUIT"
    
    print("\n")                                         # - Prints the intial menu
    for x in range(len(list_options)-1,-1,-1):          #
        print(list_options[x])                          #
    print(f"\u001b[33m-----QUIT\u001b[0m")              #
    list_options.insert(0,"QUIT")                       #

###################################
##        START THE LOOP         ##
##        CHECK USER INPUT       ##
###################################
    running = True
    while running:   
        tty.setraw(sys.stdin)                               # - Get and analyze raw keyboard iput using two steps
        char = sys.stdin.read(1)                            #
        escape_sequence = ''                                #
        if ord(char) == 27:                                 #
            escape_sequence = '\x1b' + sys.stdin.read(2)    # - capture the escape character for use later

        restore_settings()                                  # - stop using raw input mode; it's not needed after we determine the character input each loop cycle

###################################
##        HANDLE ENTER KEY       ##
###################################
        if ord(char) == 3:                                  # - check if user hitting CTRL+C to end the program, if so, quit
            running = False                                 #

        if char in ['\n','\r']:                             # - Check if key pressed was the enter key

            if nav == 0:                                    # - Check if user chose to quit, if so, quit
                clear_screen()                              #
                running = False                             #

            else:                                           # - User didn't quit, determine and execute whichever menu option was selected
                clear_screen()                              
###################################
##   CALL EXTERNAL FUNCTOINS     ##
###################################
                tempname = list_menu_methods[nav-1]         # - save typing later

                module_name = tempname[0:tempname.index(".")]

                if module_name[0] == '*':                                                   #Import from a directory up
                    working_directory = os.path.dirname(os.path.abspath(__file__))          #
                    parent_dir = os.path.dirname(working_directory)                         #
                    sys.path.insert(0,parent_dir)                                           #
                    module_name = module_name[1:]                                           #
                
                       # - Define module name dynamically by parsing argument, then create a module object to call later
                mod = importlib.import_module(module_name)      #  

                if "(" in tempname:                                                             # - '(' was in the parsed argument
                                                                                                # - means the function being called had arguments of its own, gotta hanle them

                        passed_method = tempname[tempname.index(".")+1:tempname.index("(")]     # - parsing out module name and args
                        checkargs = tempname[tempname.index("(")+1:tempname.index(")")]         #

                        executing_function = getattr(mod,passed_method)                         # - define and execute a function with provided arguments
                        executing_function(checkargs)                                           #

                else:                                                                           # - Lack of '(' tells us there were no arguments in the passed function
                        passed_method = tempname[tempname.index(".")+1:]                        # - handlling is easier        
                        executing_function = getattr(mod,passed_method)                         #
                        executing_function()                                                    #

                        
                x = input("press any key to return")        # - Give the user a break in case they want to see the output from the prior run menu option
                clear_screen()                              #

                nav = 0                                     # - prep the menu to reutn to it
                clear_screen()                              #
                print("\n")                                 #
                for x in range(len(list_options)-1,0,-1):   #
                    print(list_options[x])                  #
                print(f"\u001b[33m-----QUIT\u001b[0m")      #

###################################
##        HANDLE ARROW KEYS      ##
###################################

        else:                                               # - Key pressed earlier wasn't the enter key, deterine what it was
            if escape_sequence == '\x1b[A':                 # - It was the UP-Arrow
                if 0 <= nav < len(list_options)-1:
                    
                    nav +=1                                 # - Tell the prgram we're moving our selection up, move the cursur up a line to handle the menu activity
                    sys.stdout.write(f'\x1b[1A')            #
                
                    sys.stdout.write(f'\x1b[{nav}A')        # - Handle cursur movement based on nav variable
                    sys.stdout.write('\x1b[2K\r\x1b[K')     #
                    sys.stdout.flush()                      #
                    
                    print(f"\u001b[33m-----{list_options[nav]}\u001b[0m ")      # - Highlight the currently selected menu item, print each other item below
                    for x in range(nav):                                        #
                        sys.stdout.write("\u001b[1000D")                        #
                        sys.stdout.write('\x1b[2K\r\x1b[K')                     #
                        print(f"\u001b[0m{list_options[nav-1-x]}")              #

                else:                                           # - If the top item is selected and the up arrow is hit, cycle to the bottom
                    nav = 0                                     #
                    clear_screen()                              #
                    print("\n")                                 #
                    for x in range(len(list_options)-1,0,-1):   #
                        print(list_options[x])                  #
                    print(f"\u001b[33m-----QUIT\u001b[0m")      #


            if escape_sequence == '\x1b[B':                     # - User hit the DOWN-Arrow
                
                if 0 < nav <= len(list_options):                # - Check where cursur is, handle all situations above the bottom option
                    nav -= 1                                    #
                    clear_screen()                              #
                    print('\n')                                 #

                    for x in range(len(list_options)-1,-1,-1):  # - print menu options under the highlighted option

                        if x != nav:                            # - if the menu item isn't the selected one, list it
                            print(f"{list_options[x]}")         #

                        else:                                                           # - Otherwise, print the selected menu item
                            print(f"\u001b[33m-----{list_options[nav]}\u001b[0m ")      #

                else:                                                           # - Already at the bottom option and user hit the DOWN-Arrow, cycle it to the top
                    nav = len(list_options)-1                                   #
                    clear_screen()                                              #
                    print('\n')                                                 #
                    print(f"\u001b[33m-----{list_options[nav]}\u001b[0m ")      #
                    for x in range(len(list_options)-2,-1,-1):                  #
                        print(list_options[x])                                  #

###################################
##        END THE LOOP           ##
###################################
    clear_screen()  # - Program loop was ended, clear the screen



def option1():                  # - Used to test function handling in the main program for functions without arguments
    # clear_screen()            #
    print("Called option1")     #
    
# navigate_menu(['First Option', 'Second option', 'Third option'],["option1","menu_program_2","text_rain(abcdefghijklmnopqrstuvwzyyyyyy ...yes, that ws intentional - z)"])


###################################
##        DEFAULT FUNCTION       ##
###################################

if __name__ == "__main__":                                                                          # - Set the default function if the module is imported
    if 0 < len(sys.argv) < 3:                                                                       # Parse the provided strings into useable lists of arguments
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


