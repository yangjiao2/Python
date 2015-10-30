# Son Tu 82584074 and Yang Jiao 82222745  ICS 31 Lab sec 6.  Lab asst 7.

# e) Modify your copy_file function
print ('e)')
def copy_file(para:str):
    '''takes no parameters and returns no value
    (because it does all its work by prompting the user and reading and writing files)'''
    infile_name = input("Please enter the name of the file to copy: ")
    infile = open(infile_name, 'r', errors='ignore')
    outfile_name = input("Please enter the name of the new copy:  ")
    outfile = open(outfile_name, 'w')


    if para == 'line numbers':
        ''' the copied file includes line numbers at the start of each line '''
        infileread = infile.readlines()
        
        outfile.write (formating(infileread))
    
    elif para == 'Gutenberg trim':
        '''  if its parameter is 'Gutenberg trim' it will copy only the body of a Project Gutenberg file,
        omitting the "housekeeping" material at the front and end. '''
        infileread = infile.readlines()
        copied_list = infileread
        for line in infileread:
            if "*** START" in line:
                start_line_num = infileread.index(line)
            elif "*** END" in line:
                end_line_num = infileread.index(line)
                break
            
        copied_list = copied_list[start_line_num: end_line_num + 1]
        for i in copied_list:
            outfile.write(i)

    elif para == 'statistics':
        infileread = infile.readlines()
        copied_list2 = infileread        
        for line in copied_list2:
            outfile.write(line)
        outfile.write(stat(copied_list2))

    
    elif para == None:
        for line in infile:
            outfile.write(line)

    elif para != 'line numbers' and para != 'Gutenberg trim' and para != 'statistics':
        print ('Sorry, the parameter doesn\'t exist. \n')

    infile.close()
    outfile.close()

def formating(file:list) -> str:
    ''' return the format for the 'line number' para '''
    result = ''
    for i in range(len(file)):

            line_number = str(len(str(len(file))))
            result += ('{:'+line_number+'}: {}\n').format(str(i + 1), file[i])
    return result

def stat(lst:list) -> str:
    ''' takes a list, return the statistics needed for the 'statistics' parameter '''
    empty_line, line, total_char = 0, 0, 0
    result = ''
    line = len(lst)
    for string in lst:
        if string.strip() == "":
            empty_line += 1
        total_char += len(string.strip())

    space_for_int = (str(len(str(line))+ 1))
    space_for_float = (str(len(str(line)) + 3.1))
    
    result = ('\n{:'+ space_for_int +'}   lines in the file\n{:'+ space_for_int +'}   empty lines\n{:'+ space_for_float +'f} average characters per line\n{:'+ space_for_float +'f} average characters per non_empty line\n').format(line, empty_line, total_char / line, total_char/ (line - empty_line))
    return result

#copy_file('line numbers')
#copy_file('Gutenberg trim')
#copy_file('statistics')
#copy_file('wrong para')