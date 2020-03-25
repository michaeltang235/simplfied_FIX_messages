
# ---------------------------------------------------------------------------------
# This script uses fake FIX message file (.txt) created in fixmessage.py
# to do the following calculations
# Task 1: get message amount per client (tag1)
# Task 2: get list of all traded products (symbols)
# Task 3: get the most popular order type (tag40)
# Task 4: get average ordered quantity per product
# Task 5: get mean, max., min., median prices for the most popular product traded

# March 25, 2020
# ---------------------------------------------------------------------------------

# import modules required
import numpy as np
#
# input simplified FIX messages (txt) file
f = open('fixmsg.txt', 'r')

# read all lines of input file and save each line as a string in a list
msglist = f.readlines()


# ---------------------------------------------------------------------------------
# Task 1: get message amount per client (tag1)

# initiate client_dict dictionary to store client id (key) and its msg. count (value)
client_dict = {}

# get client id from each line of msglist using for loop
for line in msglist:
    msgparts = line.split('|')   # separate string by vertical bar '|'
    clientmsg = msgparts[8]   # get client id tag and value from the eighth item of the split list
    clientid = clientmsg[2:]   # obtain value (client id) of tag by getting all remaining entries of the item

    if clientid in client_dict:   # check if client id already exits in clientdict
        client_dict[clientid] += 1   # if yes, increment the count by 1
    else:
        client_dict[clientid] = 1   # if not, set it as 1

print('Task 1: msg. count per clint: ')
# print msg. count per client by accessing client_dict
for key in client_dict:
    print('client id = ' + str(key) + ', msg. count = ' + str(client_dict[key]))

print('\n')

# ---------------------------------------------------------------------------------

# Task 2: get list of all traded products (symbols)

# create product_list to store all traded products
product_list = []

# get traded product (symbol_id) using for loop
for line in msglist:   # for each line in msglist
    msgparts = line.split('|')   # separate string by vertical bar '|'
    productmsg = msgparts[2]   # get product msg. tag and value from the second item of the split list
    symbolid = productmsg[3:]  # obtain value (symbol_id) of tag by getting all remaining entries of the item

    if symbolid not in product_list:   # check if symbol_id already does not exit in productlist
        product_list.append(symbolid)   # append item to list if item does not exist

print('Task 2: List of all traded products:')
for item in product_list:
    print(item)
print('\n')

# ---------------------------------------------------------------------------------

# Task 3: get the most popular order type (tag40)

# create order type dictionary
ordtype_dict = {}

for line in msglist:   # for each line in msglist
    msgparts = line.split('|')   # separate string by vertical bar '|'
    ordtypemsg = msgparts[5]  # get order type msg. tag and value from the fifth item of the split list
    ordtype = ordtypemsg[3:]  # obtain value (order type) of tag by getting all remaining entries of the item

    if ordtype in ordtype_dict:   # check if order type already exits in ordtype dict
        ordtype_dict[ordtype] += 1   # if yes, increment the count by 1
    else:
        ordtype_dict[ordtype] = 1   # if not, set the count as 1

# get all values of ordtype_dict
ordtype_values = ordtype_dict.values()

# get max. value from the list
max_ordtype_value = max(ordtype_values)

# create max. ordtype key list
maxordtypekey = []

# retrieve matching key with value in ordtype_dict using for loop
for key, value in ordtype_dict.items():
    if value == max_ordtype_value:
        maxordtypekey.append(key)

# map list into string for printing output
keystring = map(str, maxordtypekey)

print('Task 3: the most popular order type: ' + ','.join(keystring))
print('\n')

# ---------------------------------------------------------------------------------

# Task 4: get average ordered quantity per product

# create order quantity dictionary to store
# product as key and quantity traded as value
ordqty_dict = {}


for line in msglist:   # for each line in msglist
    msgparts = line.split('|')   # separate string by vertical bar '|'

    productmsg = msgparts[2]  # get product msg. tag and value from the second item of the split list
    symbolid = productmsg[3:]  # obtain value (symbol_id) of tag by getting all remaining entries of the item

    ordqtymsg = msgparts[4]  # get order type msg. tag and value from the fourth item of the split list
    ordqty = ordqtymsg[3:]  # obtain value (order type) of tag by getting all remaining entries of the item

    if symbolid not in ordqty_dict:   # if symbol_id does not exist in ordqty_dict
        ordqty_dict[symbolid] = [ordqty]   # add the ordered quantity to ordqty_dict
    else:
        ordqty_dict[symbolid].append(ordqty)   # else, append to the list of ordered quantities


# create avg. ordqty dictionary with
# product as key and avg. quantity as value
avg_ordqty_dict = {}

# use a loop to calculate mean for each value under each key
for key in ordqty_dict:
    listqtystr = ordqty_dict[key]   # get list of quantity traded for each product
    listqtyint = [int(item) for item in listqtystr]   # convert each item in list str to int
    avgqty = round(np.mean(listqtyint),2)   # get mean of qty. traded and round it to 2 decimal places
    avg_ordqty_dict[key] = avgqty   # assign the resulted avg. qty. traded to avg_ordqty_dict

# output results
print('Task 4: get average ordered quantity per product:')
for key in avg_ordqty_dict:
    print(key + ', avg. ord. qty. = ' + str(avg_ordqty_dict[key]))

print('\n')

# ---------------------------------------------------------------------------------

# Task 5: get mean, max., min., median prices for the most popular product traded

# create lenqtylist to store length of each list of qty. for each product traded
lenqtylist = []
for key in ordqty_dict:
    curlenqty = len(ordqty_dict[key])   # get current length of list of qty.
    lenqtylist.append(curlenqty)   # append the length to lenqtylist

# e.g. qty list with five items means the product has been traded for 5 times
# get the max. length of qty. list to get the most popular product
maxlenqty = max(lenqtylist)

# create mpopkey list for storing the key for most popular product traded in the ordqty_dict
# a list is used in case there are more than one product sharing the same freq. of trading
# i.e. more than one product having the same number of times being traded
mpopkey = []
for key in ordqty_dict:
    curlenqty = len(ordqty_dict[key])   # get current length of qty. traded for each key
    if curlenqty == maxlenqty:   # find the key corresponding to the most popular product
        mpopkey.append(key)   # get the key to the list of mpopkey

# create symbol_id list for storing list of product symbols
# create price list for storing price for each transaction (message)
symbollist = []
pricelist = []
for line in msglist:   # for each line in msglist
    msgparts = line.split('|')   # separate string by vertical bar '|'

    productmsg = msgparts[2]  # get product msg. tag and value from the second item of the split list
    symbolid = productmsg[3:]  # obtain value (symbol_id) of tag by getting all remaining entries of the item
    symbollist.append(symbolid)   # append symbol_id to the list of symbol

    pricemsg = msgparts[9]  # get price tag and value from the ninth item of the split list
    price = pricemsg[3:-1]  # obtain value (price) of tag by getting all entries [3:second last] of the item
    pricelist.append(price)   # append price to the list of price


# create price index list for storing indices of most popular
# symbol_id in symbollist (list of products traded)
priceindex = []

# mpopkey stores symbol_id for most popular product(s) traded
# use list comprehension to get indices of all entries of
# symbol_id in the list matching that of mpopkey
for i in range(0, len(mpopkey)):
    priceindex.append([index for index, value in enumerate(symbollist) if value == mpopkey[i]])

# create mpopprice list for storing prices corresponding to the most popular product(s) traded
mpopprice = []

# use list comprehension to get entries in price list using price indices
# for each most popular product traded
for i in range(0, len(mpopkey)):
    curlistp = [pricelist[pindex] for pindex in priceindex[i]]   # current list of prices
    mpopprice.append(curlistp)   # append list of prices to mpopprice

# create mpoppricefloat for storing floating variables
mpoppricefloat = []

# use list comprehension to convert each str to float for further calculations
for i in range(0, len(mpopprice)):
    curlistpf = [float(item) for item in mpopprice[i]]   # current list of prices, converting it from str to float
    mpoppricefloat.append(curlistpf)   # append converted list of floating var. to list of mpoppricefloast

# calculate mean, max., min., and median prices for each popular product traded
# print results
print('Task 5: get mean, max., min., median prices ($) for most popular product(s) traded')
for i in range(0, len(mpopkey)):
    pricestr = ('product: ' + mpopkey[i] + ', mean = ' + str(round(np.mean(mpoppricefloat[i]),2)) +
                ', max. = ' + str(max(mpoppricefloat[i])) + ', min. = ' +
                str(min(mpoppricefloat[i])) + ', median = ' + str(round(np.median(mpoppricefloat[i]), 2)))
    print(pricestr)


































