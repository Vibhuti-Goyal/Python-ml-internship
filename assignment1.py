'''#question 1
n1=float(input("Enter the first number: "))
n2=float(input("Enter the second number: "))
sum=n1+n2
print("The sum of ",n1,"and ",n2,"is: ",sum)
print("\n")

#question 2
num=int(input("Enter the number: "))
if(num%2==0):
    print(num,"is an even number")

else:
    print(num,"is an odd number")

print("\n")

#question 3
n3=int(input("Enter the number: "))
fac=1
for i in range(1,n3+1):
    fac*=i

print("the factorial of ",n3,"is: ",fac)
print("\n")


#question 4
name=input("Enter you name: ")
print("Good morning",name)
print("\n")


#question 5
inp=input("Enter the string: ")
filename="Textfile.txt"
with open(filename,"w") as f:
    f.write(inp)
print("\n")

#question 6
filename="Textfile.txt"
with open(filename,"r") as f:
    content=f.read()
print(content)
print("\n")


#question 7
str1=input("Enter the string: ")
length=len(str1)
print("The length of",str1,"is: ",length)
print("\n")


#question 8
string1=input("Enter first string: ")
string2=input("Enter second string: ")
string3=string1+string2
print("The concatenated string is: ",string3)
print("\n")


#question 9
stri=input("Enter the string: ")
substring=input("Enter the substring: ")
if substring in stri:
    print(substring,"is present in ",stri)
else:
    print(substring,"is not present in ",stri)
print("\n")


#question 10
str0=input("Enter string: ")
print(str0.upper())
print("\n")

#question 12
num0 = input("Enter number: ")
sum = 0
for i in num0:
    if i.isdigit():
        sum += int(i)

print("The sum of digits of", num0, "is:",sum)

#question 13
year=int(input("Enter your birth year: "))
currentyear=2024
age=currentyear-year
print("Age is: ",age)
print("\n")

#question 14
lines=[]
while True:
    line=input("Enter line: ")
    if not line:
        break
    lines.append(line)
for i in lines:
    print(i)
print("\n")


#question 17
str8=input("Enter string: ")
print("The original string is: ",str8)
strf=str8.split()
strfi=""
for i in strf:
    l=len(i)
    strcap=i[0].upper()+i[1:l]+" "
    strfi+=strcap
print("The modified string is: ",strfi)
print("\n")


#question 18
str9=input("Enter first string: ")
str10=input("Enter second string: ")
if(len(str9)!=len(str10)):
    print("The strings are not anagrams")
else:
    list1=[]
    list2=[]
    for i in str9:
        list1.append(i)
    list1.sort()
    for j in str10:
        list2.append(j)
    list2.sort()

    if list1==list2:
        print("the two strings are anagram")
    else:
        print("The two strings are not anagram")
print("\n")


#question 19
stra=input("Enter the string: ")
stra2=""
l1=[]
l2=[".","!","?","()",";",":",",","-"]
for i in stra:
    l1.append(i)

for q in l1:
    if q in l2:
        continue
    
    else:
        stra2+=q

print(stra2)
print("\n")


#question 20
n=int(input("Enter the length of list you want: "))
list1=[]
for i in range(n):
    a=int(input(f"Enter the number {i+1}: "))
    list1.append(a)
sum=0
for j in list1:
    sum+=j
print(f"The sum of numbers in list {list1} is: {sum}")
print("\n")


#question 21
lists=["he","yes",2,2,55,8,True,False,2,11.67]
element=input("Enter the element you want to  counts the occurrences of: ")
count=0
for i in lists:
    j=str(i)
    if j==element:
        count+=1
print(f"The number of times {element} occurs is: {count}")
print("\n")

#question 22
lists=[2,5,7,4,90,122]
min=lists[0]
max=lists[0]
for i in lists:
    if i<min:
        min=i
    if i>max:
        max=i

print(f"The maximum and minimum values from {lists} are: {max} and {min} respectively")
print("\n")


#quetsion 23
units=input("Enter units: celcius(c)/Fahrenheit(f): ")
temp=float(input(f"Enter temperature in {units}: "))
if units.lower()=="c":
    t=(9*temp/5)+32
    print(f"The temperature {temp} celcius in Fahrenheit is: {t} ")

elif units.lower()=="f":
    t=(temp-32)*5/9
    print(f"The temperature {temp} Fahrenheit in celcius is: {t} ")
else:
    print("Invalid input")
print("\n")


#question 24
operator=input("Enter the operator you want to use(/,+,-,*): ")
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
res=0
if operator=="+":
    res=a+b
    print(f"The output of adding {a} and {b} is {res}")
elif operator=="-":
    res=a-b
    print(f"The output of subtracting {a} and {b} is {res}")
elif operator=="*":
    res=a*b
    print(f"The output of multiplying {a} and {b} is {res}")
elif operator=="/":
    res=a/b
    print(f"The output of dividing {a} and {b} is {res}")

else:
    print("Invalid input")

print("\n")


#question 26
string1=input("Enter the word: ")
l=len(string1)

p=input("Enter the prefix: ")
s=input("Enter the suffix: ")
if string1[0]==p and string1[l-1]==s:
    print(f"The prefix of {string1} is same as {p} and suffix is same as {s}")
elif string1[0]==p:
    print(f"The prefix of {string1} is same as {p}")
elif string1[l-1]==s:
    print(f"The sufix of {string1} is same as {s}")


else:
    print("none of them are same")
print("\n")'''

#question 27
strings=input("Enter string: ")
l=[]
for i in strings:
    l.append(i)
print(f"The list of characters of {strings} is {l}")