#imports
import pandas as pd
from lxml import etree

#open output text file
#***results will be reported in text file***
output = open('Pt4.txt','w')
output.write('Eliot Stanton\nLIS487 Project 2\nPart 4\n')

#parse budget
bud = etree.parse('budgets.xml')
root = bud.getroot()

output.write('\n1. Emails and Categories of Purchases Less Than $5.00\n\n')

#XPATH for elements under 5.00
results = root.xpath("//budget_item[amount<5.0]/email | //budget_item[amount<5.0]/category")

#write to text file in form email: category
for r in results:
    if (r.tag=="email"):
        output.write(r.text + ":\n")
    else:
        output.write("\t" + r.text + "\n")


output.write('\n2. Sorted Dates that People Bought Items in Computers Category:\n\n')

#list for dates
d = []

#XPATH for dates in Computer Category
results = root.xpath("//budget_item[category=\"Computers\"]/date")

#add date to list
for r in results:
    d.append(r.text)

#sort list
d.sort()
#add dates in sorted order to text file
for date in d:
    output.write(date + "\n")

output.write('\nFirst Names of People with Purchases in 2017-03:\n\n')

#XPATH for first names from 2017-03
results = root.xpath("//budget_item[date[contains(.,'2017-03')]]/name/firstname")

#add each name to text file
for r in results:
    output.write(r.text + "\n")


output.close()
