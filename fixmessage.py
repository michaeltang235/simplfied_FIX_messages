
# ----------------------------------------------------------------------
# This script generates simplified FIX messages
# Please enter number of messages required when executing the script
# output messages are written in file named 'fixmsg.txt'
# can execute the script on terminal by typing python fixmessage.py 500
# where 500 stands for number of output messages required

# created on March 25, 2020
# ----------------------------------------------------------------------

# import modules required:
import sys
import random


# check if input argument is given when calling the script on terminal
# if no input argument is given, raise index error and print error message
if len(sys.argv) < 2:
   raise IndexError("Missing input argument. Please enter number (int) of messages wanted.")


# set nummsg as the first element of command-line argument, which is the number of messages wanted
nummsg = int(sys.argv[1])
#nummsg = 30

# set output text file name, then open and write file
filename = 'fixmsg.txt'
f = open(filename, 'w')

# From the simplified rules on FIX message, some of the tags have restricted values,
# define dictionary fixdict to store tags and their corresponding values
# for detailed information on what these values represent,
# refer to https://www.onixs.biz/fix-dictionary/4.2/fields_by_tag.html
fixdict = {'54': ['1', '2'],
           '40': ['1', '2', '3', '4', '5'],
           '59': ['0', '1', '2', '3', '4', '5', '6'],
           '167': ['FUT', 'OPT', 'CS']}


for item in range(nummsg):

    # assign values to tags,
    # e.g. v55 = 4 means assign value of 4 to tag 55

    # symbol number for product name
    v55 = random.randint(1,30)   # random integer within [1,30], for the Dow Jones Index 30 constituents

    # randomly choose value from fixdict['54'] (1=buy, 2=sell) for tag54: side
    v54 = random.choice(fixdict['54'])   # buy=1, sell=2

    v38 = random.randint(1,100000)   # order quantity, number of shares or equity within [1,1000000]
    v40 = random.choice(fixdict['40'])   # order type, 1=Market, 2=Limit, 3=Stop, ...
    v59 = random.choice(fixdict['59'])   # time in force, 0=Day, 1=Good Till Cancel, ...
    v167 = random.choice(fixdict['167'])   # security type, 'FUT'=future, 'OPT'option, ...
    v1 = random.randint(1,10)   # client id, random integer within [1,10]
    v44 = round(random.uniform(0,1000),2)   # price to sell or buy, round to 2 decimal places,

    # assemble message using values obtained above, with order of tags arranged
    msg = ('8=FIX.4.2|35=D|55=SYMBOL_' + str(v55) + '|54=' + str(v54) +
           '|38=' + str(v38) + '|40=' + str(v40) + '|59=' + str(v59) +
           '|167=' + v167 + '|1=' + str(v1) + '|44=' + str(v44))

    #print(msg)

# output message to file
    f.write(msg + '\n')

# close and save output file after the loop
f.close()