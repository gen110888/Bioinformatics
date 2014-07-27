#MSIT/MIT 2nd Year 1st Semester
#IT 440 Bioinformatics
#Exercise 3.1
#by: Genesis Gonzales and Khris Macatol

#Hi Ma'am Frances Vega, this program runs best in Python 3.x.

#Division of labor:
#Genesis Gonzales - created the random sequence syntax part of the program.
#Khris Macatol - created the input length syntax part of the program.

#Group work strategy:
#1. We created our individual assigned task.
#2. We combined our work together to finish the overall task.

import random

length=int(input("Please enter the length of the random DNA sequence: "))
print()

print("The random DNA sequence is...")


sequence=""

for i in range(0,length):
    sequence+=random.choice(["A","T","C","G"])


print(sequence)

print()
input("Press enter to quit.")

#End.
