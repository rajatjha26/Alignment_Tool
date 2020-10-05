# -*- coding: utf-8 -*-

import re
import sys
import getopt
import inspect


def PrintLog(message="Here....."):
    callerframerecord = inspect.stack()[1]    # 0 represents this line
                                                # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    print ("LOG: %s:, %s:, %s:, %s" %(info.filename, info.function, info.lineno, message))

def segRemove(intermediateFile,string,romanused,setfun):
    PrintLog("Removing SegmentId's containing "+string)
    final=''
    if(setfun):
        if(romanused):
            final=re.sub(r"\(r\).txt","_segRemoved.txt",intermediateFile)
        else:
            final=re.sub(r".txt","_segRemoved.txt",intermediateFile)
    else:
        final=re.sub(r"_paraMerged.txt","_segRemoved.txt",intermediateFile)
    interm=open(intermediateFile,'r')
    finalFile=open(final,'w')
    count=0
    for line in interm:
        if(re.search(r"%s"%string,line)):
            finalFile.write("\n")
            count=count+1
        else:
            finalFile.write(line)
    PrintLog("Total "+str(count+1)+" SegmentId is replaced with newline.")

def paraMerge(inputFile,string,romanused,setfun):
    intermediate_file=''
    PrintLog("Merging Paragraphs...")
    if(romanused):
        intermediate_file=re.sub(r"\(r\).txt","_paraMerged.txt",inputFile)
    else:
        intermediate_file=re.sub(r".txt","_paraMerged.txt",inputFile)
    inp=open(inputFile,'r')
    intermed=open(intermediate_file,'w')
    paraChunk=""
    count=0
    for line in inp:
        if(re.search(r"%s"%string,line)):
            if(paraChunk != ""):
                intermed.write(paraChunk.strip())
                intermed.write("\n")
                paraChunk=""
            intermed.write(line)
        else:
            paraChunk=paraChunk.strip()+" "+line.strip()
            count=count+1
    PrintLog("Total "+str(count)+" paragraph merged")
    intermed.write(paraChunk.strip())
    intermed.close()
    if(setfun==0):
        segRemove(intermediate_file,string,0,0)


def start():
    setfun=0
    romanused=0
    src_text_file=""
    substStr=""
    try:
        options, remainder = getopt.getopt(sys.argv[1:], 'hi:s:[-p,-m,-r]:',['ifile=','subs=','roman','paraMerge','segreplace', 'help'])
    except getopt.GetoptError:
        print ('paraMerger.py -i <inputfile> -s <substitute> [-r] [-m] [-p]')
        sys.exit(2)
    print(options)
    for opt, arg in options:
        if opt in ('-h', '--help'):
            print("Usage: \
                \n -i --input file, \
                \n -s, --substitute str, \
                \n -r, --roman, \
                \n -p, --paraMerge, \
                \n -m, --segreplace, \
                \n -h, --help")
            print('coammand: \
            \n paraMerger.py -i <inputfile> -s <substitute> [-r] [-m] [-p]')
            sys.exit(1)	
        elif opt in ('-i', '--ifile'):
            src_text_file = arg
            print('input file=%s'%arg)
        elif opt in ('-s', '--subs'):
            substStr = arg
            print("string to be substituted= "+substStr)
        elif opt in ('-r', '--roman'):
            print("in roman")
            romanused=1
            src_text_read=open(src_text_file,'r')
            stringFile=[]
            for line in src_text_read:
                line=re.sub(r"০|०|૦|੦|௦",str(0),line)
                line=re.sub(r"১|१|૧|੧|௧",str(1),line)
                line=re.sub(r"২|२|૨ |੨|௨",str(2),line)
                line=re.sub(r"৩|३|૩|੩|௩",str(3),line)
                line=re.sub(r"৪|४|૪|੪|௪",str(4),line)
                line=re.sub(r"৫|५|૫|੫|௫",str(5),line)
                line=re.sub(r"৬|६|૬|੬|௬",str(6),line)
                line=re.sub(r"৭|७|૭|੭|௭",str(7),line)
                line=re.sub(r"৮|८|૮|੮|௮",str(8),line)
                line=re.sub(r"৯|९|૯|੯|௯",str(9),line)
                stringFile.append(line)
            src_text_read.close()
            change_srcFile=src_text_file.replace(".txt","")+"(r)"+".txt"
            f=open(change_srcFile,"w")
            for line in stringFile:
                f.write(str(line))
                f.write("\n")
            f.close()
            src_text_file=change_srcFile
        elif opt in ('-p', '--paramerge'):
            # print(1)
            setfun=1
            paraMerge(src_text_file,substStr,romanused,setfun)
        elif opt in('-m','--segreplace'):
            # print(2)
            setfun=1
            segRemove(src_text_file,substStr,romanused,setfun)
    if(setfun==0):
        # print(3)
        paraMerge(src_text_file,substStr,romanused,setfun)
start()
