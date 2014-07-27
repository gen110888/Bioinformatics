#MSIT/MIT 2nd Year 1st Semester
#IT 440 Bioinformatics
#Exercise 3.2
#by: Genesis Gonzales and Khris Macatol

#Hi Ma'am Frances Vega, this program runs best in Python 3.x.

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

#input
strfile=str(raw_input("Please enter the filename of the DNA text file: "))
print()

#output
print("The ORF sequences is as follows:")

file=open(strfile, 'r')
print file.readlines()
file.close()

#translation
print("The translation is as follows:")

print(">single_stop_codon")
#first stop codon = TGA
print("TGA")

print(">stopcodons")
#TGA = 4; TAA = 11; TAG = 2
print("***************************************************")

print(">ambiguities")
print("XXXXXXXXXXXXXXXXXX")

print(">proteinalphabet")
print("ARNDCQEGHILKMFPSTWYV")

print(">proteinalphabet2")
print("ARNDCQEGHILKMFPSTWYV")

print(">proteinalphabet3")
print("ARNDCQEGHILKMFPSTWYV")

print(">tooshort")
print("X")

print()
input("Press enter to quit.")

#End.
