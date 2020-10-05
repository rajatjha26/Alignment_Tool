# -*- coding: utf-8 -*-
import re

data=open("almora-mar.txt","r")

stringFile=[]

for line in data:
    line=re.sub(r"০|०|૦|੦|௦",str(0),line)
    line=re.sub(r"১|१|૧|੧|௧",str(1),line)
    line=re.sub(r"২|२|૨ |੨|௨",str(2),line)
    line=re.sub(r"৩|३|૩|੩|௩",str(3),line)
    line=re.sub(r"৪|४|૪|੪|௪",str(4),line)
    line=re.sub(r"৫|५|૫|੫|௫",str(5),line)
    line=re.sub(r"৬|६|૬|੬|௬",str(6),line)
    line=re.sub(r"৭ |७|૭|੭|௭",str(7),line)
    line=re.sub(r"৮|८|૮|੮|௮",str(8),line)
    line=re.sub(r"৯|९|૯|੯|௯",str(9),line)
    stringFile.append(line)


for line in stringFile:
    print(line)