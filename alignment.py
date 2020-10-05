from nltk import tokenize
import re

class Alignment:

    def paragraghSplit(self,fileName):
        Para=""
        self.fileName=fileName
        file=open(self.fileName,"r")
        for line in file:
            if(line.strip()):
                Para=Para+line
        # remove blank line from the input file
        Blanklinerem=re.sub(r"(\s)*\n(\n)*(\s)*","\n",Para,re.MULTILINE | re.IGNORECASE | re.UNICODE)
        # split paragraphs and insert each paragraph into list
        split_para=Blanklinerem.split("\n")
        return(split_para)
    
    def sentenceSplit(self,engPara,hinPara):
        self.engPara=engPara
        self.hinPara=hinPara
        P=1
        sentenceArray=[]
        for engText,hinText in zip(self.engPara,self.hinPara):
            pref="P"+str(P)
            sentenceEnders = re.compile(r"""(?:(?<=[\|!?])|(?<=[\।]))\s+""",re.MULTILINE |re.UNICODE)
            hinSen = sentenceEnders.split(hinText)
            engSen=tokenize.sent_tokenize(engText)
            # print(engSen,hinSen)
            s=1
            eng,hin="",""
            for eng,hin in zip(engSen,hinSen):
                main_pref=pref+"."+str(s)
                sentence=str(main_pref)+"|"+str(eng)+"|"+str(hin)
                s=s+1
                sentenceArray.append(sentence)
            for remEng in range(engSen.index(eng)+1,len(engSen)):
                main_pref=pref+"."+str(s)
                sentence=str(main_pref)+"|"+engSen[remEng]+"|"+" "
                s=s+1
                sentenceArray.append(sentence)
            for remHin in range(hinSen.index(hin)+1,len(hinSen)):
                sentence=" "+"|"+" "+"|"+hinSen[remHin]
                sentenceArray.append(sentence)
            P=P+1
        return(sentenceArray)
    
    def segmentAlign(self,para_eng,para_hin):
        if(len(para_eng)==len(para_hin)):
            return True
        paraFIle=open("SegmentLog.txt","w")

        for eng,hin in zip(para_eng,para_hin):
            paraFIle.write(eng[0:50])
            paraFIle.write("    ")
            paraFIle.write(hin[0:50])
            paraFIle.write("\n")
        return False
    
    def sentenceAlign(self,alignedSen):

        self.alignedSen=alignedSen
        outFIle=open("AlignSentence.csv","w")
        for sen in self.alignedSen:
            outFIle.write(sen)
            outFIle.write("\n")


ali=Alignment()
para_eng=ali.paragraghSplit("Munnar_eng.txt")
para_hin=ali.paragraghSplit("Munnar_hin.txt")

if(ali.segmentAlign(para_eng,para_hin)):
    alignSen=ali.sentenceSplit(para_eng,para_hin)
    ali.sentenceAlign(alignSen)

else:
    print("Check SegmentLog.txt and align the segments.")
