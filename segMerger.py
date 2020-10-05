file=open("AlignSentence.csv","r")

csvData=""
for data in file:
    csvData=csvData+data

csvData=csvData.split("\n")

newData="Paraid|English|Hindi"
seg=0
for data in csvData:
    if(data):
        para,_=data.split(".",1)
        para=int(para.replace("P",""))
        
        if(para>seg):
            seg=para
            if(seg<10):
                newData=newData+"\n"+"\"#SEG00"+str(seg)+"\"|"+"\"#SEG00"+str(seg)+"\"|"+"\"#SEG00"+str(seg)+"\""
            elif(seg>9 and seg<100):
                newData=newData+"\n"+"\"#SEG0"+str(seg)+"\"|"+"\"#SEG0"+str(seg)+"\"|"+"\"#SEG0"+str(seg)+"\""
            else:
                newData=newData+"\n"+"\"#SEG"+str(seg)+"\"|"+"\"#SEG"+str(seg)+"\"|"+"\"#SEG"+str(seg)+"\""
        newData=newData+"\n"+data
print(newData)
