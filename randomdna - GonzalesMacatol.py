#MSIT/MIT 2nd Year 1st Semester
#IT 440 Bioinformatics
#Exercise 3.1: randomdna
#by: Genesis Gonzales and Khris Macatol

#Hi Ma'am Frances Vega, this program runs best in Python 2.x.
#Also, the random DNA sequence output cuts to the next line every after 60th character
#to be similar to your samples as Fasta format.

#Division of labor:
#Genesis Gonzales - created the random sequence syntax part of the program.
#Khris Macatol - created the input length syntax part of the program.

#Group work strategy:
#1. We created our individual assigned task.
#2. We combined our work together to finish the overall task.

#Start.

import random

b=True
while(b):
    length=0

    try:
        length=int(input('Please input the length of the random DNA sequence then press "Enter": '))
    except:
        continue
    print ""

    print(">myrandomsequence")


    sequence=""

    for i in range(0,length):
        
        sequence+=random.choice(["A","T","C","G"])
        if(len(sequence)%60==0):
            print(sequence)
            sequence=""


    print(sequence)

    print""
    while True:
        inpt=raw_input('Please press "Enter" to input the length of the random DNA sequence again or input "Q" / "q" then press "Enter" to quit: ')

        if(inpt=="Q" or inpt=="q" or inpt=="" or inpt=="\n"):
            break

    if(inpt=="Q" or inpt=="q"):
        break

#End.
