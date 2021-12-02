#Eliot Stanton
#LIS 487
#Regex Project
#Part One

#import re and codecs
import re
import codecs

#****READING FILE****
#open the html file, read it, and close it
file = codecs.open('Henry V Entire Play.html','r','utf-8')
alltext = file.read()
file.close()

#split and extract only the text after the header
at = alltext.split('</table>')
fulltext = at[1]

#****FORMAT TEXT AND REMOVE HTML****

#remove html and reformat headings, special format for Act and Scene headings
fulltext = re.sub('<h3>(ACT.*)</h3>','== \\1 ==',fulltext)
fulltext = re.sub('<h3>(SCENE.*?)\.\s(.*)</h3>','== \\1 ==\n\n{' +'\\2}'.strip(),fulltext)
fulltext = re.sub('<h3>(.*?)</h3>','\\1',fulltext)

#remove html and reformat stage directions with brackets
fulltext = re.sub('(<p>)?<i>(.*)</i>(</p>)?','[\\2]',fulltext)

#remove html and reformat name of who is speaking
fulltext = re.sub('<a name="speech.*<b>(.*)</b></a>','\\1:',fulltext)

#remove html and reformat text of their speech to indent
fulltext = re.sub('<a name="\d.*?>(.*)</a><br>','\t\\1',fulltext)

#remove any bracketed html that remains with text in between
pat = re.compile('<(.*?)>(.*?)</\\1>',re.S)
fulltext = re.sub(pat,'\\2',fulltext)

#adjust line spacing so text blocks have one blank line between them (not two)
fulltext = re.sub('\\n\\n\\n','\\n\\n',fulltext)

#remove any remaining html
fulltext = re.sub('<.*?>','',fulltext)

#adjust line spacing so text blocks have one blank line between them (not zero)
fulltext = re.sub('(\t.*?\n)(\S)','\\1\\n\\2',fulltext)

#print(fulltext)

#***WRITING TO FILE***
alldone = open('HenryV.txt','w')
alldone.write(fulltext)
alldone.close()
