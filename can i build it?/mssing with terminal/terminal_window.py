
import sys, subprocess, time, termios, tty
import readline



def navigate_menu(list_options:list, list_menu_methods:list=None):
    
    oldval = [27906, 5, 1215, 35387, 15, 15, [b'\x03', b'\x1c', b'\x7f', b'\x15', b'\x04', b'\x00', b'\x01', b'\x00', b'\x11', b'\x13', b'\x1a', b'\xff', b'\x12', b'\x0f', b'\x17', b'\x16', b'\xff', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00']]
    
    subprocess.run('clear',shell=True)
    nav = 0
    
    # print(list_options)
    print("\n")
    for x in range(len(list_options)-1,-1,-1):
        print(list_options[x])
    print(f"\u001b[33m-----QUIT")
    list_options.insert(0,"QUIT")
    

    running = True
    while running:
        tty.setraw(sys.stdin)   # <----  require keyboard input to be processed in its raw form which is broken into three 2-digit numbers or escape characters
        char = sys.stdin.read(1)   # <----   capture the first input 2-digit # or escape code
        escape_sequence = ''
        if ord(char) == 27:
            escape_sequence = '\x1b' + sys.stdin.read(2)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldval)
        if ord(char) == 3:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldval)
            running = False
        if char in ['\n','\r']:
            if nav == 0:
                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldval)
                subprocess.run('clear',shell=True)
                running = False
            else:
                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldval)
                globals()[list_menu_methods[nav-1]]()
                x = input("press any key to return")
                nav = 0
                subprocess.run('clear',shell=True)
                print("\n")
                for x in range(len(list_options)-1,0,-1):
                    print(list_options[x])
                print(f"\u001b[33m-----QUIT")

        else:
            if escape_sequence == '\x1b[A':
                if 0 <= nav < len(list_options)-1:
                    # print(f"increasing nav from {nav} to {nav+1}, the list is {len(list_options)} long")
                    nav +=1
                    sys.stdout.write(f'\x1b[1A')
                # for x in range(nav):
                    sys.stdout.write(f'\x1b[{nav}A')
                    sys.stdout.write('\x1b[2K\r\x1b[K')
                    sys.stdout.flush()

                    
                    print(f"\u001b[33m-----{list_options[nav]}\u001b[0m ")
                    for x in range(nav):
                        sys.stdout.write("\u001b[1000D")
                        sys.stdout.write('\x1b[2K\r\x1b[K')
                        print(f"\u001b[0m{list_options[nav-1-x]}")

                else:
                    nav = 0
                    subprocess.run('clear',shell=True)
                    print("\n")
                    for x in range(len(list_options)-1,0,-1):
                        print(list_options[x])
                    print(f"\u001b[33m-----QUIT")


            if escape_sequence == '\x1b[B':
                
                if 0 < nav <= len(list_options):
                    nav -= 1
                    subprocess.run('clear',shell=True)
                    print('\n')

                    for x in range(len(list_options)-1,-1,-1):
                        if x != nav:
                            print(f"{list_options[x]}")
                        else:
                            print(f"\u001b[33m-----{list_options[nav]}\u001b[0m ")

                else:
                    nav = len(list_options)-1
                    subprocess.run('clear',shell=True)
                    print('\n')
                    print(f"\u001b[33m-----{list_options[nav]}\u001b[0m ")
                    for x in range(len(list_options)-2,-1,-1):
                        print(list_options[x])
    
    subprocess.run('clear',shell=True)

def call_func(func):
  func()

def option1():
    subprocess.run('clear',shell=True)
    print("option1")
    

navigate_menu(['First Option', 'Second option', 'Third option'],["option1"])
