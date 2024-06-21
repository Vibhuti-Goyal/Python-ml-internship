
"""
#LIST
str1="Hello all!"
list1=list(str1)
print("the new list formed is: ",list1)
print(str1.split())
print("\n")
list2=[1,2,3,"hey",3+7j]
print("the original list is: ",list2)
list2.append("new_value")
print("the updated list is: ",list2)
print("\n")
list2.insert(2,70)
print(list2)
print("\n")

list3=[1,3,6,"yes",23.56]
list4=[1,4,2,"no"]
print("Original list is: ",list3)
list3.extend(list4)
print("The updated list is: ",list3)
print("list concatination: ",list3+list4)
print("\n")
print("original list is: ",list4)
list4[1:3]=[6,10]
print("modified list is: ",list4)

print("\n")
print("original list is: ",list4)
list4[1:3]=[6,10,"heyy","owl"]
print("modified list is: ",list4)

list5=["hello","bye",1,10,90]
print("the original list is: ",list5)
list5.remove("hello")
print("the updated list is: ",list5)
print("\n")
list5=["hello","bye",1,10,90,"Hello","hello"]
print("the original list is: ",list5)
list5.remove("hello")
print("the updated list is: ",list5)

list6=["hello","bye",1,10,90,"Hello","hello"]
print("the original list is: ",list6)
print(list6.count("hello"))
#sorting only works when we have same type of elements in list
# error occured
# list6.sort()
# print("the sorted list is: ",list6)

print("\n")
list7=[2,94,81,10,4]
list7.sort()
print("The sorted list is: ",list7)
list7.sort(reverse=True)
print("reverse sorted list is: ",list7)


#TUPLE
tup1=(1,2,"hello","bye",True)
print("the original tuple is: ",tup1)
tup2=tuple((1,2,"hey","yes",False))
print("new tuple is: ",tup2)
tup3=tuple([1,2,"hey","yes",False])
print("new list tuple is: ",tup3)
#TUPLE FROM LIST
list1=[1,6,"ploy"]
tup0=tuple(list1)
print("tuple from list is: ",tup0)
#LIST FROM TUPLE
list2=list(tup0)
print("list from tuple is: ",list2)
#TUPLE FROM STRING
str1="hello world"
newtup=tuple(str1)
print("tuple from string is: ",newtup)
tup4=("hello")
print("The tuple is: ",tup4,"Type of tuple is: ",type(tup4))
tup5=("hello",)
print("The tuple is: ",tup5,"Type of tuple is: ",type(tup5))


tup5=("hey",11,5,8,False,11.6,5+9j)
print("The original tuple is: ",tup5)
print("The first element is: ",tup5[0])
print("Slicing of tuple: ",tup5[2:5])
print("Reverse of tuple is: ",tup5[::-1])
print("The negative slicing is: ",tup5[-7:-3])
print("The negative slicing is: ",tup5[-3:-7]) #not possible


tup6=(1,4,5,"hello","Hello",837)
print("The original tuple is: ",tup6)
print("The length of tuple is: ",len(tup6))
print("If hello is present or not: ","hello" in tup6)
print("If Hello is present or not: ","Hello" in tup6)
print("If 50 is present or not: ",50 in tup6)

tup7=(1,1,56,8,2,1)
print("the count of 1 is: ",tup7.count(1))
print("The index of 1 is: ",tup7.index(1))

"""



