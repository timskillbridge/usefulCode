


                                                        #####################################
                                                        ##        NEEDED   IMPORTS         ##
                                                        #####################################
#JUST THE TERMINAL MENU!
from terminal_menu import navigate_menu, option1

                                                        #####################################
                                                        ##     TEST WITH/WITHOUT ARGS      ##
                                                        #####################################

navigate_menu(\
    ["3x3 Random Grid (Lives in other.py located in parent directory)","Option 1","Text Rain effect","calculator"],\
        ["*other.grid3x3","terminal_menu.option1","text_rain.text_rain(This is a passed text string)","ANSI.clc"])


# - Usage:
    # Takes two arguments
        # list of entries for the menu, separated by a comma, all strings
        # list of modules and function within quotes in the module.function order, separated by a comma, all strings
            #if module is in parent directory, place a * as the first character in the module name
    # List length must match
    # Quit option will be added at runtime.