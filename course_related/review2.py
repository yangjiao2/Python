
def different(l:list)->int:
    ''' It takes a two-dimensional table as input and returns the number of
        distinct entries in the table
    '''
    counter={}
    for i in l:
        for j in i:
            if j not in counter.keys():
                counter[j]=1
            else:
                counter[j]+=1
    count = set()
    for i in l:
        for j in i:
            count.add(j)
    #print (count)
    #print (len(count))
    #print (len(counter))
different([[0,1,0],[1,0,1]])
different([[32,12,52,63],[32,64,67,52],[64,64,17,34],[34,17,76,98]])


# a
from collections import namedtuple
Customer = namedtuple('Customer' ,'id name address')

Product = namedtuple('Product', 'name cost')

Order = namedtuple('Order' , 'id total_cost items')

# b
C1= Customer(1, 'Josh', '133 Stanford')
C2 = Customer(2, 'Joanna', '133 Amherst aisle')

# c
P1 = Product ('donut', 3.55)
P2 = Product ('apple' , 1.29)
P3 = Product ('book', 2.00)
P4 = Product ('beef', 5.90)
P5 = Product ('dog food', 10.99)

# d
O1 = Order (C1.id, P1.cost * 2 + P3.cost * 4, [P1, P3])
O2 = Order (C2.id, P2.cost * 9, [P2])
print (O1)
print (O2)


# Modify
# a
P6= Product ('fish', 0.00)
O1.items.append(P6)
O2.items.append(P6)

# b
lst_of_Product = [P1].extend(P2)

# c
total_number = (len(O1.items) + len(O2.items))

# d
print (O1.items)
C1 = C1._replace(address = C1.address + ' Irvine')
O1 = O1._replace(total_cost = O1.total_cost + P6.cost)
#O1 = O1._replace(items = O1.items.append(P3))
print (C1)
print (O1)

# didn't do sort

# files
outfile = open('ppppra.txt','w')
outfile.write('Yang\nRocky Road')
outfile.close()
infile = open('ppppra.txt','r')
readfile = infile.readlines()
name = readfile[0]
fav_ice_cream = readfile[1]
print (readfile)

outfile1 = open('whatisthis.txt','w')
outfile1.write('Little love\nWill you wait for me forever\nBaby\nYou raise me up\nNever say never\nApologize\nLollipop\nIch lieb dish\nInnocent\nGirlfriend')
outfile1.close()
infile1 = open('whatisthis.txt', 'r')
'''
readfile1 = infile1.read()
fav_song = readfile1.split("\n")[0]
least_song = readfile1.split("\n")[2]
'''
least = infile1.read().split("\n")[0]
#what = infile1.read()
#print ('what',what)
#least_song = infile1.read().split()[3]
print (infile1.read())

#print ('======\n' +name  + fav_ice_cream)
print (least)

PRODUCT = [P1,P2,P3]
DIC = {}
for p in PRODUCT:
    DIC.update({p.name: p})
print (DIC)
'''

products = [p1,p2,p3,p4,p5]
product_dict = {}
for p in products:
   product_dict[p.name] = p
'''
print ('=====================')

print ('item        price\n--------------------')
for ee in O1.items:
    print (('{:8}    ${:2.2f}').format(ee.name, ee.cost))
print ('--------------------')
print (('total       ${:2.2f}').format(O1.total_cost))

print ('=====================')
