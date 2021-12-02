#Eliot Stanton
#487 Project 2
#Part 1

#imports
import pandas as pd

#read CSV into pandas dataframe
bud = pd.read_csv('XML_project.csv',names=['name','email','category','amount','date'])

#subset the dataframe to just select columns of interests
sub = bud.loc[:,['date','category','amount']]

###EXTRA CREDIT: SORTING BY DATE, LATEST TO EARLIEST###
sub = sub.sort_values(by="date",ascending=False)

#convert the subset df to html
ht = sub.to_html(index=False,justify='left')

#write the html to an html file
pt1 = open('Pt1.html','w')
pt1.write(ht)
pt1.close()
