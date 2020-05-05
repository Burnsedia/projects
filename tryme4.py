import os


# Debuging helper functions
def debug_nine():
    print('calling "nine_lines()"')

def debug_clear_screen():
    print('calling "clear_screen()"')


# core functions of script
def new_line():
    print('.')
    # using a return statment, so I can write the output to a file.
    return "."
 
def three_lines():
    # calls new line
    new_line()
    new_line()
    new_line()

def nine_lines():
    three_lines()
    three_lines()
    three_lines()

def clear_screen():
    nine_lines()
    three_lines()
    three_lines()
    new_line()

def save_output(tmp1,tmp2):
    out1= str(tmp1)
    out2 = str(tmp2)
    return out1 + out2

# main function and entry point to program. This is how you develop a python application, have a main.py and other python modules for diffent functionality an use some OOP and Data Driven 
#    Digen using DataObject if in Python 3.7 or 3.8
# def main():
#     #calling primery functins
#     debug_nine()
#     nine_lines()
#     debug_clear_screen()
#     clear_screen()
#     #writing to dick, after functions return there outputs
#     save = save_output(debug_nine,clear_screen)
#     file = open("tryme4-output.txt", "w")
#     file.write(save)
#     file.close

 
#  if __name__ == __main__():
#     main()
 
#calling primery functins
debug_nine()
nine_lines()
debug_clear_screen()
clear_screen()
#writing to dick, after functions return there outputs
# save = save_output(debug_nine,clear_screen)    
# file = open("tryme4-output.txt", "w")
# file.write(save)
# file.close