# Kayla Elias 95601331 and Yang Jiao 82222745. Lab Asst 1.

# imports os library
import os, sys
from stat import *

# FIND THE DIRECTORY:
def action_on_files_in_directory ()->:
    '''Finds all unique files in the directory, subdirectories, their subdirectories, etc.'''
    while True:
        try:
            # ask user which path to search for files and removes all spaces before and after
            path = input('Enter the path to the directory you wish to search: ').strip()
            #checks if the path exists
            if os.path.isdir(path):
                # do the rest
        except:
            print('Sorry, the directory name given does not exist.')
    
    

    

# FIND THE FILE(S) YOU WANT:
#function prints menu of choices for user to type (limits error in users imput) 
def menu_of_search_choices()->str:
    '''prints a menu of choices user can type for how to search through files in a directory'''
    menu = '{}\n{}\n{}\n'.format('1. Search by Name: Searches for files matching the name inputted.', '2. Search by Name Ending: Searches for files by type', '3. Search by Size: Searches for files by minimum number of bytes')
    print(menu)
  
def store_interesting_files()->'File':
    '''stores specific files based on users choice between 3 characteristics'''
    try:
        #  prints the choices the user can type and ask user which characteristic to search by, makes it lowercase
        menu_of_search_choices()
        search = input('Enter the number of how you wish to search files from the choices above: ').strip()
        # search by name
        if search == '1':
            return search_by_name()
        # search by name ending
        elif search == '2':
            return search_by_name_ending()
        # search by minimum bytes
        elif search == '3':
            return search_by_size()   
    except:
        print('Sorry, the directory name given does not exist.')

# Search by Name - ask user what the FULL name is
#       (files names EXACTLY match a particular name)
def search_by_name (pathname:'Path')->list:
    '''asks the user to input the FULL name of the file. Then searches for files by that name and returns the name of the file in a list'''
    try:
        #asks the user for the file name and takes away spaces before and after the input
        file_name = input('Enter the full name of the file you wish to find: ').strip()
        # combines the path and the name 
        result = []
        full_name = os.path.join(pathname[, name])
        result.append(full_name)
        # search the computer for the file and store it.
        if os.path.isfile(full_name):
            return result
    except:
        print('File name does not exist. Please try again.')

#Search by Name Ending - ask user what does name end with 
#       (names that end with a particular string:.py, .txt)
def search_by_name_ending ()->:
    '''asks the user to input the name ending of the file. Then searches for files by that name ending'''
    try:
        # asks user for the file ending and takes away spaces before and after the input
        name_ending = input('Enter the name ending (i.e. .py, .txt, .doc,...) you wish to find: ').strip()
        list_of_files = os.listdir('.')
        result = []
        # finds files with the same name ending
        for a_file in list_of_files:
            if a_file.split('.')[1] == name_ending:
                result.append(a_file)
        return result
    except:
        print('Error. Name ending does not exist. Try again.')
#Search by Size - ask user what the limit should be in bytes
#          (measured in bytes, files whose size are AT LEAST that size)
def search_by_size (pathname:'Path')->list:
    '''asks the user to input the minimum size of the file. Then searches for files that match.'''
    try:
        #asks the user for the minimum bytes and strips the spaces away from the input.
        size = input('Enter the minimum size of the file (in bytes): ').strip
        list_of_files = os.listdir('.')
        result = []
        # finds all files >= the input
        for a_file in list_of_files:
            if os.path.getsize(os.path.join(pathname[,a_file])) >= size:
                result.append(a_file)
        return result
            
    except:
        print('Sorry, incorrect input. Try again.')
        












# ACTION TAKEN ON EACH INTERESTING FILE:

# creates a menu for the user to choose an input from
def action_menu()->str:
    '''prints a menu of options for the user to type to take action on the file'''
    print_path_option = '1. Print Path Only'
    print_first_line_option = '2. Print First Line of Text'
    copy_file_option = '3. Copy File'
    touch_file_option =  '4. Update File Timestamp'
    ActionMenu = '{}\n{}\n{}\n{}\n'.format(print_path_option, print_first_line_option, copy_file_option, touch_file_option)
    print(ActionMenu)


def take_action_on_file ()->:
    '''asks the user which action to take then '''
    # ask user which action should be taken on the interesting files and strips it of spaces before and after
    user_action = input('Enter the number of the action you wish to take: ')
    action = user_action.strip()

# Print Path Only - print the files path to the console
def print_path_only ()->:
    '''prints the file's path to the console'''
    print()

# Print First Line of Text - 1. open the file
#                            2. read the first line of text from the file
#                            3. print that text to the console
def print_first_line_of_text (filename:'File')->str:
    '''opens the file, reads the first line, prints that text to the console'''
    #opens the file
    open_first_line = open(filename, 'r')
    # reads the firstline
    first_line = open_first_line.readline()
    # prints the line
    print(first_line)
    # closes the file
    open_first_line.close()


# Copy File - make a copy of the file and store it in the same directory as original
#               COPY should have .copy appended to the filename
def copy_file (filename:'File')->:
    '''makes a copy of a file and stores it in the smae directory as the original with .copy added to the name'''
    #opens the file
    open_copy_file = open(filename, 'r')
    #copies the file
    # prints a done message
    done_message = 'The file has been copied under {}.copy'.format(filename)
    print(done_message)
    #closes the file
    open_copy_file.close()


    
# Touch File - modify the last modified timestamp to be current date/time
def touch_file (filename:'File')->:
    '''changes the last modified timestamp to be the current date/time'''
    #opens file
    open_touch_file = open(filename, 'r')
    # prints a done message
    done_message = 'The timestamp has been modified on {}.'.format(filename)
    #closes file
    open_touch_file.close()

    
###### NOTE: after user imput: remove spaces from beginning and end of imput
#           *** if after removing does not match a choice or wrong type(int, bool)
#               print error message and ask user to try again.
# THE PROGRAM SHOULD STILL RUN EVEN IF ONE FILE OR ONE DIRECTORY FAILS!!!
#           -RETURN AND ERROR MESSAGE AND KEEP GOING (THIS FILE DOESNT WORK)

### ADD IF _NAME_ == '_MAIN_':
#           THE_THINGS_YOU_WANT_TO_HAPPEN_ONLY_WHEN_MODULE_IS_RUN()
# returns true if module is executed not imported.

### PAY ATTENTION TO: OS. OS.PATH, AND STAT

# FIND ALL UNIQUE FILES IN THE DIRECTORY SUBDIRECTORIES THEIR SUBDIRECTORIES ETC
# by finding first the directory (no subdirectories) then the subdirectories then symbolix links


### in a separate file for testing write code that creates dirrectories, files and symbolic links 