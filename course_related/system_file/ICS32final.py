# Kayla Elias 95601331 and Yang Jiao 82222745. Lab Asst 1.

import os, sys
from stat import *

import shutil

import time
from stat import *

# MAIN PROGRAM: takes user imput and finds and verifies a path, directory, and file. Then takes an action on it based upon more user imput 
def action_on_files_in_directory ():
    '''runs the main program that finds and acts on files and directories based upon a path chosen by the user'''
    while True:
        try:
            path = input('Enter the path to the directory you wish to search: (Hit "Enter" if you want to quit.\n>>>').strip()
            
            if os.path.isdir(path):
        
                final_files = store_interesting_files(path)

                take_action_on_file (final_files)
                
            elif path == '':
                print ('Thanks! Good-bye!')
                break
            else:
                print ('Sorry, the directory does not exist.')
                
        except:
            print('Main Program Error.')
             
# SEARCH PROGRAM: Searches for files by name, name ending, and maximum byte amount then stores them. 

def menu_of_search_choices()->str:
    '''prints a menu of user choices for how to search through files in a directory'''
    menu = '{}\n{}\n{}\n'.format('1. Search by Name: Searches for files matching the name inputted.', '2. Search by Name Ending: Searches for files by type', '3. Search by Size: Searches for files by minimum number of bytes')
    print(menu)
  
def store_interesting_files(path:str)->'list of files':
    '''takes user imput and searches through files then stores them'''
    try:
        menu_of_search_choices()
        search = input('Enter the number of how you wish to search files from the choices above: ').strip()
        
        # search by name
        if search == '1':
            result = search_by_name(path)
        # search by name ending
        elif search == '2':
            result = search_by_name_ending(path)
        # search by minimum bytes
        elif search == '3':
            result = search_by_size(path)
        

        if result == None:
            store_interesting_files(path)
            
        else:
            print ('That\'s what I found:')
            print (result)            
            return result
    except:
        print ('Sorry, you should input the number of your choice, such as 1 , 2 or 3.')
        store_interesting_files(path)

# FILTERS: goes through a list of files, directories, and subdirectories based upon imput and returns the result.
def filter_file_by_name(pathname:str, filename:str, result:list)->list:
    '''goes through a list of directories within the pathname and
    returns a list of files with the specific filename the user inputted'''
    try:
        for entry in os.listdir(pathname):
            full_name = os.path.join(pathname, entry)
            if os.path.isfile(full_name) and entry == filename:
                
                result.append(full_name)

            elif os.path.isdir(full_name):
                new_pathname = full_name

                filter_file_by_name(new_pathname, filename, result)
        return result
    except:
        print ('Access denied')

        
def filter_file_by_name_ending(pathname:str, nameending:str, result:list)->list:
    '''return a list of files with specific name ending'''
    for entry in os.listdir(pathname):    
        try: 
            full_name = os.path.join(pathname, entry)
            if os.path.isfile(full_name) and os.path.splitext(entry)[1][-len(nameending):] == nameending:
                result.append(full_name)
            elif os.path.isfile(full_name) and os.path.splitext(entry)[0][-len(nameending):] == nameending:
                result.append(full_name)
            elif os.path.isfile(full_name) and entry[-len(nameending):] == nameending:
                result.append(full_name)            
            elif os.path.isdir(full_name):
                new_pathname = full_name
                filter_file_by_name_ending(new_pathname, nameending, result)
        except:
            print ('Access denied')
            
    return result
        
def filter_file_by_size(pathname:str, min_size:int, result:list)->list:
    '''return a list of files which is bigger than the minimum size'''
    for entry in os.listdir(pathname):    
        try:
            full_name = os.path.join(pathname, entry)
            if os.path.isfile(full_name) and os.path.getsize(full_name) <= min_size:
                result.append(full_name)

            elif os.path.isdir(full_name):
                new_pathname = full_name
                filter_file_by_size(new_pathname, min_size, result)

        except:
            print ('Access denied')                
    return result

# SEARCHES: takes an input and does one of the filters above.
def search_by_name (pathname:'Path')->list:
    '''asks the user to input the FULL name of the file.
    Then searches for files by that name and returns the name of the file in a list'''
    
    file_name = input('Enter the full name of the file you wish to find: ').strip()
    print ('Searching....')
    result = []
    result = filter_file_by_name(pathname, file_name, result)
    if result == []:
        print('Sorry! File name does not exist. Please try again.')
    else:
        return result

def search_by_name_ending (pathname:'Path')->list:
    '''asks the user to input the name ending of the file.
    Then searches for files by that name ending'''

    name_ending = input('Enter the name ending (i.e. .py, .txt, .doc,...) you wish to find: ').strip()
    print ('Searching....')
    result = []
    result = filter_file_by_name_ending(pathname, name_ending, result)
    
    if result == []:
        print('Sorry! Name ending does not exist. Please try again.')
    else:
        return result
        
def search_by_size(pathname:'Path')->list:
    '''asks the user to input the minimum size of the file. Then searches for files that match.'''
    
    size = eval(input('Enter the minimum size of the file (in bytes): '))
    print ('Searching....')
    result = []
    result = filter_file_by_size(pathname, size, result)    
    if result == []:
        print('Sorry! File smaller than the given size does not exist. Please try again.')
    else:
        return result
        

# ACTION TAKEN ON FILE: Takes the previously stored files and either prints the path, prints the first line, copies, or touchs the files timestamp.

def action_menu()->str:
    '''prints a menu of options for the user to type to take action on the file'''
    print_path_option = '1. Print Path Only'
    print_first_line_option = '2. Print First Line of Text'
    copy_file_option = '3. Copy File'
    touch_file_option =  '4. Update File Timestamp'
    ActionMenu = '{}\n{}\n{}\n{}\n'.format(print_path_option, print_first_line_option, copy_file_option, touch_file_option)
    print(ActionMenu)

def take_action_on_file (final_files:list):
    '''asks the user which action to take then '''
    action_menu()
    user_action = input('Enter the number of the action you wish to take: ').strip()

    if user_action == '1':
        print_path_only(final_files)
    elif user_action == '2':
        print_first_line_of_text(final_files)
    elif user_action == '3':
        copy_file(final_files)
    elif user_action == '4':
        touch_file(final_files)
    else:
        print ('Sorry, you should input the number of the choice such as 1, 2, 3, or 4.\nPlease try again')
        take_action_on_file(final_files)


def print_path_only (final_files:list)->str:
    '''prints the file's path to the console'''
    for file in final_files:
        print (file)

def print_first_line_of_text (final_files:list)->str:
    '''opens the file, reads the first line, prints that text to the console'''
   
    for file in final_files:
        print (file)
        open_file = open(file, 'r')
        first_line = open_file.readline()
        print(first_line)  
        open_file.close()

def copy_file (final_files:list)->'file':
    '''makes a copy of a file and stores it in the same directory as the original with .copy added to the name'''
    for file in final_files:
        shutil.copyfile(file, file+'.copy')
        done_message = 'The file has been copied under {}.copy'.format(file)
        print(done_message)


def touch_file (final_files:list):
    '''changes the last modified timestamp to be the current date/time'''
    for file in final_files:
        statinfo = os.stat(file)

        old_mtime = os.stat(file).st_mtime
        os.utime(file, None)
        ## If times is none, then the file access and modified times are set to the current time.
        ##The parameter times consists of row in the form of (atime, mtime) i.e (accesstime, modifiedtime).
        new_mtime = os.stat(file).st_mtime

        done_message = 'The timestamp has been modified on {} from {} to {}.'.format(file, time.ctime(old_mtime), time.ctime(new_mtime))
        print (done_message)

action_on_files_in_directory ()