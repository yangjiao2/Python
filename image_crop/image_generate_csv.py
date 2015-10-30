from PIL import Image
import os
import csv

ROWNUM = 8
COLNUM = 40

def readBox(direc, newline1, delimiter1):
    f = open(direc, newline=newline1, encoding="utf8")
    linelist = list(csv.reader(f, delimiter = delimiter1, quoting=csv.QUOTE_NONE))
    f.close()
    return linelist

def belongingRowAndColumn(imwidth, imheight, smallerhl, biggerhl, smallervl, biggervl, ROWNUM, COLNUM):
    row = -1
    col = -1
    rowwidth = imwidth/COLNUM 
    colheight = imheight/ROWNUM

    for i in range(ROWNUM):
        if smallerhl >= colheight * (i) and biggerhl <= colheight * (i+1):
            row = ROWNUM - i
            break
        elif abs(smallerhl - colheight * (i+1)) < colheight and abs(biggerhl - colheight * (i+1)) < colheight and abs(smallerhl - colheight * (i+1)) > abs(biggerhl - colheight * (i+1)):
            row = ROWNUM - i
            break

        elif abs(smallerhl - colheight * (i+1)) < colheight and abs(biggerhl - colheight * (i+1)) < colheight:
            row = ROWNUM - i - 1
            break
    
    for k in range(COLNUM):
        if smallervl >= colheight * (k) and biggervl <= colheight * (k+1):
            col = k + 1
            break
        elif abs(smallervl - rowwidth * (k+1)) < rowwidth and abs(biggervl - rowwidth * (k+1)) < rowwidth and abs(smallervl - rowwidth * (k+1)) > abs(biggervl - rowwidth * (k+1)):
            col = k + 1
            break
        elif (abs(smallervl - rowwidth * (k+1)) < rowwidth and abs(biggervl - rowwidth * (k+1)) < rowwidth):
            col = k + 1 + 1
            break
        
    RowCol = (row, col)
    if row == -1 or col == -1:
        print ('Error categorizing row and column:')
        print ("smallerhl: ", smallerhl, "biggerhl: ", biggerhl)
        print ("smallervl: ", smallervl, "biggervl: ", biggervl)
        print ("Row iter and Col iter: ", i, k)
        print ("Row and Col: ", RowCol)
    
    return RowCol
            

def generatecsvtable(cropCoordinate, file, ROWNUM, COLNUM):
    table = []
    for line in cropCoordinate:
        (symbol, lowerleftx, lowerlefty, upperrightx, upperrighty, ignore) = line
        height = int(upperrighty) - int(lowerlefty)
        width = int(upperrightx) - int(lowerleftx)
        if height != 0 or width != 0:
            image = Image.open(file)
            (imwidth, imheight) = image.size
            position = belongingRowAndColumn(imwidth, imheight,  int(lowerlefty), int(upperrighty), int(lowerleftx), int(upperrightx), ROWNUM, COLNUM)
            table.append([symbol, position])
    csvtable = [[""] * (COLNUM + 1)] * (ROWNUM + 1)
    firstline  = [""]
    for k in range(ROWNUM + 1):
        csvtable[k] = [k] + ['']*(COLNUM - 1)
    for i in range(1, COLNUM+1):
        firstline.append(str(i))
    csvtable[0] = firstline
    

    for item in table:
        temp = csvtable[item[1][0]][item[1][1]]
        csvtable[item[1][0]][item[1][1]] = temp  + item[0] + "_"

    return [table, csvtable]

if __name__ == "__main__":
    boxfile = 'C:\\Users\\Yang\\Desktop\\test2\\test2.box'
    newline = '\n'
    delimiter = ' '
    cropCoordinate = readBox(boxfile, newline, delimiter)
    imagefile = "C:\\Users\\Yang\\Desktop\\test2\\test2.png"
    csvfile = "C:\\Users\\Yang\\Desktop\\test2\\test2.csv"
    [table, csvtable] = generatecsvtable(cropCoordinate, imagefile, ROWNUM, COLNUM)

    ofile  = open(csvfile, 'w', newline='',  encoding='utf-8')
    writer = csv.writer(ofile,  delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for row in csvtable:
        try:
            writer.writerow(row)
        except:
            print ('Error writing to file: ', row)
    ofile.close()
    
        
    

