'''import keyword as k

#to see keywords in python
print(k.kwlist)
print(len(k.kwlist))

#INPUT OUTPUT
num=int(input("Enter number: "))
print(num)
print(type(num))

#typecasting-> changing one datatype to another datatype
#methods-> int(), str(), float()

print(1,2,3,4,sep="%",end="@")

#WRITE IN TEXT FILE
sampleopen= open("C:/Users/Vibhuti/Desktop/notes/Python ml internship/file demo.txt",'w')
print(1,2,3,4,sep="%",end="@",file=sampleopen)

#USING FORMAT
print("hello all {} people in class".format(10))
print("hello all {} people in {}".format(10,"class"))

print(0b101)
print(0B1011)

import random
print(random.randrange(20,50))
print(random.random())
#TO PIC ANY VALUE FROM SEQUENCE

List1=["Hello","bye","go"]
print(random.choice(List1))
random.shuffle(List1)
print(List1)'''

import math as mt
print(mt.factorial(5))
print(mt.pow(2,3))
print(mt.log10(1000000))

