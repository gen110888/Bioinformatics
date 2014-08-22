#MSIT/MIT 2nd Year 1st Semester
#IT 440 Bioinformatics
#Exercise 3.2: translatedna
#by: Genesis Gonzales and Khris Macatol

#Hi Ma'am Frances Vega, this program runs best in Python 2.x.
#Also, the random DNA sequence output cuts to the next line every after 60th character
#to be similar to your samples as Fasta format.

#Division of labor:
#Genesis Gonzales - created part of the program.
#Khris Macatol - created part of the program.

#Group work strategy:
#1. We created our individual assigned task.
#2. We combined our work together to finish the overall task.

#Start.

items={"GCT":"Ala", "GCC":"Ala", "GCA":"Ala", "GCG":"Ala","CGT":"Arg", "CGC":"Arg", "CGA":"Arg", "CGG":"Arg", "AGA":"Arg", "AGG":"Arg","AAT":"Asn", "AAC":"Asn","GAT":"Asp", "GAC":"Asp","TGT":"Cys","TGC":"Cys","CAA":"Gln", "CAG":"Gln","GAA":"Glu","GAG":"Glu","GGT":"Gly", "GGC":"Gly", "GGA":"Gly", "GGG":"Gly","CAT":"His", "CAC":"His","ATT":"Ile", "ATC":"Ile", "ATA":"Ile","ATG":"Start","TTA":"Leu", "TTG":"Leu", "CTT":"Leu", "CTC":"Leu", "CTA":"Leu", "CTG":"Leu","AAA":"Lys","AAG":"Lys","ATG":"Met","TTT":"Phe", "TTC":"Phe","CCT":"Pro", "CCC":"Pro", "CCA":"Pro", "CCG":"Pro","TCT":"Ser", "TCC":"Ser", "TCA":"Ser", "TCG":"Ser", "AGT":"Ser", "AGC":"Ser","ACT":"Thr", "ACC":"Thr", "ACA":"Thr", "ACG":"Thr","TGG":"Trp","TAT":"Tyr", "TAC":"Tyr","GTT":"Val", "GTC":"Val", "GTA":"Val", "GTG":"Val","TAA":"Stop", "TGA":"Stop", "TAG":"Stop"}


filee=0

while(True):
    filename=raw_input("Please enter the filename which contains DNA sequence(s) to be translated: ")
    try:
        filee=open(filename)
        break
    except:
        continue

dnas=list()
titles=list()

for line in filee:
    if line[0]==">":
        dnas.append("")
        titles.append(line.strip())
    else:
        dnas[len(dnas)-1]+=line.strip()

filee.close()

#print(dnas)

for index in range(0,len(dnas)):
    string=dnas[index]
    title=titles[index]
    string=string.upper()

    
    print(title)
    sequence=""

    for char in string:
        
        sequence+=char
        if(len(sequence)%60==0):
            print(sequence)
            sequence=""

    print(sequence)

    ambiguities=0

    newString=""
    for i in string:
        if(i not in ("A", "T", "C", "G")):
            ambiguities+=1
        else:
            newString+=i

    stopCodons=set()

    for i in range(0,len(newString),3):
        if newString[i:i+3] in ("TGA","TAA","TAG"):
            stopCodons.add(newString[i:i+3])

    if "TGA" in newString:
        stopCodons.add("TGA")
    if "TAA" in newString:
        stopCodons.add("TAA")
    if "TAG" in newString:
        stopCodons.add("TAG")

    stopCodonsTxt=""

    for item in stopCodons:
        stopCodonsTxt+=item

    print(">stopcodons")

    print(stopCodonsTxt)

    print(">ambiguities")
    print(ambiguities*"X")

    for l in range(0,3):
        if(l!=0):
            print(">proteinalphabet"+str(l+1)+" ARNDCQEGHILKMFPSTWYV")
        else:
            print(">proteinalphabet ARNDCQEGHILKMFPSTWYV")      

        newString2=""
        newString2+=newString[:l]+" "
        for i in range(l,len(newString),3):
            if newString[i:i+3] in ("TGA","TAA","TAG"):
                newString2+=","
            else:
                if(i+3<=len(newString)):
                    newString2+=newString[i:i+3]+" "
                else:
                    newString2+=newString[i:]+" "

        newString3=newString2.strip()

        newString3=newString3.split(",")
        #print(newString3)

        maxStrings=list()

        for item in newString3:
            if(len(maxStrings)==0):
                maxStrings.append(item.strip())
            else:
                if(len(maxStrings[0])<len(item.strip())):
                    maxStrings=list()
                    maxStrings.append(item.strip())
                elif(len(maxStrings[0])==len(item.strip())):
                    maxStrings.append(item.strip())

        #print(maxStrings)
        term=""
        term2=""
        for i in range(0,len(maxStrings)):          
            
            tooshort=True
            maxi=0
            for x in maxStrings[i].split():
                maxi=max(maxi,len(x))
                if(len(x)==3):
                    tooshort=False
                    term+=items[x]
                    term2+=x
                    term+="-"
                    term2+="-"

            if(tooshort):
                print ""
                print(">tooshort")
                print("X"*maxi)
                break
                    
            term=term[:-1]
            term2=term2[:-1]
            
            if(i+1<len(maxStrings)):
                term+=" and "
                term2+=" and "

       

        if(len(term)!=0):
            print(term2)
            print(term)
            print(">tooshort")
            print ""

    inpt=0
    while True:
        inpt=raw_input('Please press "Enter" to translate the next DNA sequence or input "Q" / "q" then press "Enter" to quit: ')

        if(inpt=="Q" or inpt=="q" or inpt==""):
            break

    if(inpt=="Q" or inpt=="q"):
        break
    
#End.
