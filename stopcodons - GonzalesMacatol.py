#MSIT/MIT 2nd Year 1st Semester
#IT 440 Bioinformatics
#Exercise 3.2: stopcodons
#by: Genesis Gonzales and Khris Macatol

#Hi Ma'am Frances Vega, this program runs best in Python 2.x.
#Also, the random DNA sequence output cuts to the next line every after 60th character
#to be similar to your samples as Fasta format.

#Division of labor:
#Genesis Gonzales - created the translate DNA program.
#Khris Macatol - researched the answers to the following questions.

#Group work strategy:
#1. We created our individual assigned task.
#2. We combined our work together to finish the overall task.

#Answers:
#1. The "stop codon" in the standard code is a nucleotide triplet within messenger RNA 
#that signals a termination of translation. It is also called as the termination codon.
#2. We are talking about a "standard code" because it defines how sequences of codons 
#specify which amino acid will be added next during protein synthesis and 
#since the vast majority of genes are encoded with exactly the same code then this particular code 
#is often referred to as the canonical or standard genetic code or simply the genetic code.
#3. Looking for the longest ORF to find genes in eukaryotes will not work because 
#there are large non-coding regions between genes and introns in genes. 
#mRNA undergoes processing before translation. A protein-encoding gene 
#may contain stop codons within intronic regions. PTMs make gene prediction even more difficult. 
#4. Our code is found below.
#5. We structure our code in a way wherein 
#6. Our code below is tested and found out that the requirements are fulfilled.
#7. The longest protein snippet produced on the file an_exon.dna is the Os07g32390.1 11977.m07504.

#References:
#http://en.wikipedia.org/wiki/Stop_codon
#http://en.wikipedia.org/wiki/Codon
#http://www.molecularsciences.org/book/export/html/29

#Start.

items={"GCT":"Ala", "GCC":"Ala", "GCA":"Ala", "GCG":"Ala","CGT":"Arg", "CGC":"Arg", "CGA":"Arg", "CGG":"Arg", "AGA":"Arg", "AGG":"Arg","AAT":"Asn", "AAC":"Asn","GAT":"Asp", "GAC":"Asp","TGT":"Cys","TGC":"Cys","CAA":"Gln", "CAG":"Gln","GAA":"Glu","GAG":"Glu","GGT":"Gly", "GGC":"Gly", "GGA":"Gly", "GGG":"Gly","CAT":"His", "CAC":"His","ATT":"Ile", "ATC":"Ile", "ATA":"Ile","ATG":"Start","TTA":"Leu", "TTG":"Leu", "CTT":"Leu", "CTC":"Leu", "CTA":"Leu", "CTG":"Leu","AAA":"Lys","AAG":"Lys","ATG":"Met","TTT":"Phe", "TTC":"Phe","CCT":"Pro", "CCC":"Pro", "CCA":"Pro", "CCG":"Pro","TCT":"Ser", "TCC":"Ser", "TCA":"Ser", "TCG":"Ser", "AGT":"Ser", "AGC":"Ser","ACT":"Thr", "ACC":"Thr", "ACA":"Thr", "ACG":"Thr","TGG":"Trp","TAT":"Tyr", "TAC":"Tyr","GTT":"Val", "GTC":"Val", "GTA":"Val", "GTG":"Val","TAA":"Stop", "TGA":"Stop", "TAG":"Stop"}

b=True
while(b):
    print('Please input the DNA sequence to be translated then press "Enter": ')

    string=raw_input()
    string=string.upper()

    print(">single_stop_codon")

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


    while True:
        inpt=raw_input('"Enter" to go back from start or "Q":')

        if(inpt=="Q" or inpt=="q" or inpt=="" or inpt=="\n"):
            break

    if(inpt=="Q" or inpt=="q"):
        break

#End.
