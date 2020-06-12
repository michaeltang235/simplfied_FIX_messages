# simplfied_FIX_messages
Financial Information eXchange (FIX) is an open source protocol widely used to trade all asset types in the global financial systems. It provides a machine-readable data that can be shared between dealers and institution clients for communicating trade information. 

In this repository, a set of simplified rules are implemented to generate a series of fake FIX 4.2 messages. An example is given below.

8=FIX.4.2|35=D|55=SYMBOL_1|54=1|38=100|40=2|59=0|167=FUT|1=CLIENT_1|44=199.99 

Each message field is delimited by a vertical bar '|', and each field is specified by a tag and its corresponding value. For instance, the message field (54=1) has a tag of 54 and a value of 1. Each tag and the associated value has its own meaning. In the example given, tag of 54 represents the field 'side', while a value of 1 denotes the action of 'Buy'. For further details of the meaning of them, please refer to the website of FIX protocol documentation,

https://www.onixs.biz/fix-dictionary/4.2/fields_by_tag.html

The set of simplified rules adopted are given below,

8=FIX.4.2 (always this value)
35=D (always a new order message ‘D’)
55=SYMBOL_N (Symbol meaning the product name: N is a number) Note that in real life this could be a stock like GOOGLE
54=[1-2] side (buy or sell the given symbol/product)
38=N (quantity of the symbol/product that you want to buy or sell)
40=[1-5] (only order types 1-5 per the FIX 4.2 spec: http://btobits.com/fixopaedia/fixdic42/tag_40_OrdType_.html)
59=[0-6] (all time in force orders per FIX 4.2 spec: https://www.onixs.biz/fix-dictionary/4.2/tagNum_59.html)
167=(FUT|OPT|CS) (Futures, Options and Common stocks)
1=CLIENT_N (random client id)
44=Any price (price at which you will sell or buy the given product)


There are two scripts presented in this repository. \\
(1): The first one named fixmessage.py intakes the number of fake FIX messages interested as a command-line input argument and generates the required lines of messages with randomly chosen values for each tag, outputing the results into a .txt file named 'fixmsg.txt'.

e.g. issuing the follwoing command on terminal

python fixmessage.py 1000

generates 1000 random and simplified FIX 4.2 messages written in a file called fixmsg.txt


(2): The second one named fixmsg_stats.py takes the messages files written in part (1) and perform the following calculations to obtain statistical insights on the messages generated. 

Task 1: get message amount per client (tag1)\
Task 2: get list of all traded products (symbols)\
Task 3: get the most popular order type (tag40)\
Task 4: get average ordered quantity per product\
Task 5: get mean, max., min., median prices of the most popular product traded






