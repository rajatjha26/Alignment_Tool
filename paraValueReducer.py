import re

file=open("ahmedabad_new.txt","r")

newData=""
for data in file:
    newData=newData+data
j=0
for i in range(200):
    if(re.search(r"P(%s)[.](\d)"%str(i),newData)):
    	newData=re.sub(r"P(%s)[.](\d)"%str(i),r"P%s.\2" %str(j),newData)
    	j=j+1
print(newData)
