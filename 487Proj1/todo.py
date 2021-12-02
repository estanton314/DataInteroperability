#Eliot Stanton
#LIS 487
#Regex Project
#Part Two

#import re and codecs
import re
import codecs

#*****READING FILE*****
#open todo.txt, read it line by line, and close it
file = codecs.open('todo.txt','r','utf-8')
alltext = file.readlines()
file.close()

#*****DEFINING REGEX PATTERNS*******
#regex patterns to match correctly-formatted names, phone numbers, dates, and emails
namepat = re.compile('([A-Z][a-z]*-)?[A-Z][a-z]*\s([A-Z]).?\s?[A-Z]?\w*(\s[A-Z][a-z]*)?')
numberpat = re.compile('\(\d{3}\)-\d{3}-\d{4}')
datepat = re.compile('\d{4}-\d\d?-\d\d?')
emailpat = re.compile('\w*@\w*.com')

#dictionary to contain fully-formatted tasks as values, with dates as the keys
finaldict = {}

#****LOOP THROUGH TASKS*****
#iterate through each task one by one
for line in alltext:

    #***FORMATTING PARTS OF TASKS****
    clean = line

    #format date as yyyy-(m)m-(d)d
    clean = re.sub('(\d\d?)/(\d\d?)/(\d{4})','\\3-\\1-\\2',clean)
    clean = re.sub('(\d\d?)-(\d\d?)-(\d{4})','\\3-\\1-\\2',clean)

    #format phone number as (###)-###-####
    clean = re.sub('(\d{3}).*?(\d{3}).*?(\d{4})','(\\1)-\\2-\\3',clean)

    #move date to the front of the task with a space separating it from other text
    clean = re.sub('(.*?)(\d{4}-\d\d?-\d\d?)(.*)','\\2 \\1\\3',clean)
    #add a 0 before any single digit day or month
    clean = re.sub('-(\d)([-\s])','-0\\1\\2',clean)

    #remove extra parentheses or country code from before phone number
    clean = re.sub('(.*?)[1\-\(]*(\(\d{3}\)-\d{3}-\d{4})(.*)','\\1\\3 \\2 ',clean)
    #separate email from other text with a space on either side
    clean = re.sub('(.*?)(\w*@\w*.com)(.*?)', '\\1 \\2 \\3',clean)

    #****EXTRACTING PARTS OF TASKS****

    #find name, number, date, and email in the cleaned task using regex defined outside loop
    name = namepat.search(clean).group()
    number = numberpat.search(clean)
    if number == None:
        number = ""
    else:
        number = number.group()
    date = datepat.search(clean).group()
    email = emailpat.search(clean)
    if email == None:
        email = ""
    else:
        email = email.group()

    #find the task description by splitting on regex for all other parts
    tasksplit = re.split('\(\d{3}\)-\d{3}-\d{4}|\d{4}-\d\d?-\d\d?|\w*@\w*.com|(?:[A-Z][a-z]*-)?[A-Z][a-z]*\s(?:[A-Z]).?\s?[A-Z]?\w*(?:\s[A-Z][a-z]*)?',clean)
    taskdesc = ""
    for i in tasksplit:
        #adding all other text to the task description
        if i!=None:
            taskdesc = taskdesc + i
    #remove leading and trailing spaces and commas, and extra spaces between words
    taskdesc = re.sub('[\s,]*(.*)','\\1',taskdesc)
    taskdesc = re.sub('(.*?)([\s,]+)$','\\1',taskdesc)
    taskdesc = re.sub('(.*?)(\s\s+)(.*)','\\1 \\3',taskdesc)

    #***COMBINING FORMATTED PARTS INTO FORMATTED TASK*****

    #combine the task parts in the proper format
    finalline = date + ": " + taskdesc + "\n\t" + name + ", " + number + email
    #add the formatted task to the dictionary stored with its date as its key
    finaldict[date]=finalline

#****WRITING TO FILE*****
alldone = open('Tasks.txt','w')
#adding tasks in sorted order of their dates
for key in sorted(finaldict):
    #print(finaldict[key])
    alldone.write(finaldict[key] + '\n')
alldone.close()
