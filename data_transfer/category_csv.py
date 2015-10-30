import csv
category = ['Acadamic', 'Misc.', 'Misc. entertainment', 'Email', 'Serious news', 'Online service', 'Social Media', 'Shopping', 'Busiiness', 'Gaming', '000']

MENU = 'Found a website does not fit in the standard category.\n'
CAT = """
1. acadamic
2. misc.
3. misc. entertainment
4. email
5. serious news
6. online service
7. social media
8. shopping
9. business
10. gaming
11. unknown
>>
"""
INTEGER_INPUT = 'Please input an integer.'
unknown_website = set()
unknown_row = []
unknown_row_num = []
unknown_website_num = []
with open('400URL_coded_YW_YJ_final.csv') as file1:
    readfile1 = csv.reader(file1)
    dict1 = dict()
    for row in list(readfile1)[1:]:
        dict1[row[0]] = row[2]
##
##def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
##    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
##    for row in csv_reader:
##        yield [unicode(cell, 'utf-8') for cell in row]
f = open('all_log_data_nocolumns_analysis.txt', 'w')
with open('all_log_data_nocolumns.csv', 'r', encoding = 'charmap') as file2:
    with open('result.csv', 'w', newline = '' ) as writingfile:
        with open('all_log_data_nocolumns_copy.csv', 'w', newline = '' , encoding = 'charmap') as file3:
            writing = csv.writer(file3)
            writefile = csv.writer(writingfile)
            all = []
            readfile2 = csv.reader(file2)
            row_num = 2
       
            f.write ('------------------------------------------------------------------------------------------\n')
            f.write ('Chinese app rows:\n')
            for row in readfile2:
                try:
    #                 if row[2].lower() == 'app' or row[2].lower() == 'idle' or row[2].lower() == 'activitytype' or row[2].lower() == 'system' or row[2].lower() == 'in_call' or row[2].lower() == 'out_call':
    #                     writefile.writerow(row + [row[6]])
                    if row[2].lower() == 'url':
                        website = row[6]
                        if website.find('://') != -1:
                            website = website[website.index('://') + 3:]
                        if website.find('www.') != -1:
                            website = website[website.index('www.') + 4:]
                        if website.find('/') != -1:
                            website = website[: website.index('/')]
                        if website in dict1.keys():
                         
                
                            writefile.writerow( row + [dict1[website]])
                        else:
                            unknown_website_num.append(row_num)
                            unknown_website.add(row[6])
                       
                            writefile.writerow(row + ['Uncategorized'])
        ##                    try:
        ##                        print (MENU)
        ##                        print (website)
        ##                        print (row[6])
        ##                        cat_num = int(input(CAT).strip()) - 1
        ##                    except:
        ##                        print (INTEGER_INPUT)
        ##                        cat_num = int(input(CAT).strip()) - 1
        ##                    finally:
        ##                        while len( (input('Confirm that '+ website+' belongs to '+category[cat_num] +'.\n>>')).strip()):
        ##                            print (website)
        ##                            cat_num = int(input(CAT).strip()) - 1
        ##                        writefile.writerow(row + [category[cat_num]])
                    else:
                        
                        writefile.writerow(row+ [row[6]])
    
        
                    row_num +=1
                except:


                
                    writefile.writerow( row[0:6]+ ['Chinese character app'])
                 
                    all.append(row_num)
                    f.write(str(row_num) + ' ' + str( row) + '\n')
                    row_num +=1
    
            

f.write ('\nThe total number of the Chinese app rows are: ' + str(len(all)) + '\n')


f.write('\n\n\n------------------------------------------------------------------------------------------\n') 
f.write('Uncategorized urls: ')
for a in unknown_website:
    f.write(a + '\n')
f.write('\nThe total number of the Chinese app rows are: ' + str(len(unknown_row_num)) + '\n')
f.write('\n\n\n------------------------------------------------------------------------------------------\n')
print ('Finish')
                             
                        


                
        