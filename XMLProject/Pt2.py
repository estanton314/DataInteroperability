#Eliot Stanton
#487 Project 2
#Part 2

#imports
import pandas as pd

#open output text file
#***results will be reported in text file***
output = open('Pt2.txt','w')
output.write('Eliot Stanton\nLIS487 Project 2\nPart 2\n')

#read CSV into pandas dataframe
bud = pd.read_csv('XML_project.csv',names=['name','email','category','amount','date'])
#format amount as ##.##
bud['amount'] = bud['amount'].str.lstrip('$').astype(float)

#group by category
cats = bud.groupby("category")

#lists to hold categories and their totals
cat = []
total = []

#iterate through each category
for name,data in cats:
    #sum the amounts from each row in the category
    n = round(sum(data['amount']),2)
    #add to lists
    cat.append(name)
    total.append(n)

#attach categories and their totals in a dataframe
final = pd.DataFrame({'Category':cat,'Total':total})

output.write('\n1. Total Amounts for Each Budget Category \n\n')

#add line to text file for each row in the form "category: $total"
i=0
while i < len(final):
    output.write(final.iloc[i,0]+ ":\n\t$" + str(final.iloc[i,1])+ "\n")
    i=i+1

output.write('\n2. Category People Spent the Most Money In\n\n')

#sort categories by total and take the highest one
max = final.sort_values(by='Total',ascending=False).reset_index().loc[0]

#add line to text file for max category
output.write('They spent the most of any budget category, $' + str(max['Total']) + ', on ' + max['Category'] + " items.\n")

#get date in form YYYY-MM
bud['ym']=bud['date'].str[0:7]

#make dictionary to hold dates and totals
ym = {}
i = 0

#iterate over each purchase
while i<len(bud):
    #get its date and cost
    date = bud.iloc[i,5]
    n = bud.iloc[i,3]
    #add its cost to the dictionary under the entry for the date
    if (date in ym):
        ym[date]=ym[date]+n
    else:
        ym[date]=n
    i = i+1

output.write('\n3. Total Amounts for Each Year-Month\n\n')

#add a line in the text file for each year-month and the total spent in the form "YYYY-MM: $total"
for key in sorted(ym.keys()):
    output.write(key + ": $" + str(round(ym[key],2))+"\n")

#sort purchases by amount and take the highest one
exp = bud.sort_values(by='amount',ascending=False).reset_index().loc[0]

output.write('\n4. Person Who Spent Most Money on Single Item\n\n')

#add a line to the text file for the most expensive purchase, giving details
output.write(exp['name'] + " bought the most expensive item; they spent $" + str(exp['amount'])
 + " on the date " + exp['date'] + " to buy something from the category " + exp['category'] + ".\n")

#close output
output.close()
