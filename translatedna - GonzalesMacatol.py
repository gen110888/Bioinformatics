#MSIT/MIT 2nd Year 1st Semester
#IT 440 Bioinformatics
#Exercise 3.3
#by: Genesis Gonzales and Khris Macatol

#Hi Ma'am Frances Vega, this program runs best in Python 3.x.

#Division of labor:
#Genesis Gonzales - created part of the program.
#Khris Macatol - created part of the program.

#Group work strategy:
#1. We created our individual assigned task.
#2. We combined our work together to finish the overall task.

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
print("***************************************************")

print(">alphabet_gene")
print("ARNDCQEGHILKMFPSTWYV")

print(">alphabet_gene2")
print("ARNDCQEGHILKMFPSTWYV")

print()
input("Press enter to quit.")

#End.
