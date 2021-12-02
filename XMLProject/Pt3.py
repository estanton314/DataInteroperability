#Eliot Stanton
#487 Project 2
#Part 3

#imports
from lxml import etree
import csv

#read in csv file
csvfile = open('XML_project.csv')
#read csv into lines
fileLines = csv.reader(csvfile, delimiter=',')

#open the xml file
xmlout = open('budgets.xml','w')

#write header text to xml file (version, encoding, namespace/scheme)
xmlout.write('''<?xml version="1.0" encoding="UTF-8"?>
<budget xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="budgets.xsd">
''')

#iterate through each budget item
for f in fileLines:

    #split name into parts (first and last)
    name = f[0].split()
    #deal with people who have a space in their first name (De witt)
    if (name[0]=='De'):
        fn = name[0]+" " + name[1]
        ln = name[2]
    #assume all others have a single first name and spaces are multiple last names
    else:
        fn = name[0]
        ln = ""
        for i in range(1,len(name)):
            ln = ln + name[i] + " "

    #extract email, category, amount, and date of item
    email = f[1]
    category = f[2]
    amount = float(f[3].lstrip('$'))
    date = f[4]

    #combine all parts into XML form for a single budget item
    s = '''
    <budget_item>
        <name>
            <firstname>%s</firstname>
            <lastname>%s</lastname>
        </name>
        <email>%s</email>
        <amount>%s</amount>
        <category>%s</category>
        <date>%s</date>
    </budget_item>
    ''' % (fn,ln,email,amount,category,date)

    #add the item to the XML file
    xmlout.write(s)

#close the root item (budget)
xmlout.write("\n</budget>")

#close the csv and the xml files
csvfile.close()
xmlout.close()

#parse the schema in budgets.xsd
xmlschema_doc = etree.parse("budgets.xsd")

#use the parsed schema to create an XMLSchema object
xmlschema = etree.XMLSchema(xmlschema_doc)

#read in the XML file we just wrote, to validate it
doc = etree.parse("budgets.xml")

#check to make sure the file adheres to the schema
print(xmlschema.validate(doc))
#it prints True- yay!
