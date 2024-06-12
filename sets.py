#SETS
#set doesnot consider true 
'''set1={1,4,2,2,3,5,"hello","hello",1,"bye",True,False}
print("The set is: ",set1)
set1.add(90)
print("The updated set is: ",set1)
list1=[1,2,3,4,5,6,7]
set1.update(list1)
print("The updates set is: ",set1)

set2={2,1,3,4,5}
print("The original set is: ",set2)
set2.remove(5)
print("The removed set is: ",set2)
#if we try to remove the value again, it will show error if value is not found
set2.discard(0)
print("The discarded set is: ",set2)
#discard method will not show error if value is not found



#all()->  checks for true set of boolean values
set3={True,True,True}
res=all(set3)
print(res)
set3.add(False)
res=all(set3)
print(res)
#ALL NUMBERS EXCEPT 0 ARE TRUE



#any()->if atlest one value is True
set4={True,False,0,1,234}
res=any(set4)
print(res)
set4={0,0,False}
res=any(set4)
print(res)
set4={True,384,0,False,1,73}
print("Original set is: ",set4)
print("The length of set is: ",len(set4))


#max() and min() and sum()
set5={3,58,2,19,93}
res=max(set5)
print("The maximum value is: ",res)
res=min(set5)
print("The minimum value is: ",res)
res=sum(set5)
print("The sum of all values in set is: ",res)


#MATHEMATICAL SET OPERATIONS
#1. UNION->COMBINES UNIQUE VALUES OF SET A AND B
set8={1,2,3,4,5}
set9={3,4,5,6,7}
print("The union of sets through first method is: ",set8.union(set9))
print("The union of sets through second method is: ",set8|set9)

#2.INTERSECTION-> TAKES ONLY COMMON ELEMENTS IN BOTH SETS
set8={1,2,3,4,5}
set9={3,4,5,6,7}
print("The intersection of sets through first method is: ",set8.intersection(set9))
print("The intersection of sets through second method is: ",set8 & set9)

#3.DIFFERENCE-> A-B GIVES THOSE ELEMENTS OF A WHICH ARE NOT PRESENT IN B i.e. REMOVES COMMON ELEMENTS
set8={1,2,3,4,5}
set9={3,4,5,6,7}
print("The difference of sets through first method is: ",set8.difference(set9))
print("The difference of sets through second method is: ",set8 - set9)

#4. SYMMETRIC_DIFFERENCE-> REMOVES COMMON ELEMENTS OF BOTH SET AND PRINT UNCOMMON ELEMENTS FROM BOTH SETS
set8={1,2,3,4,5}
set9={3,4,5,6,7}
print("The symmetric difference of sets through first method is: ",set8.symmetric_difference(set9))

#5. issubset(), issuperset(), isdisjoint()
set1={1,2,3,4}
set2={1,2,3,4,5,6,7}
set3={9,0,7,8,9}
print("Set1 is subset of set2: ",set1.issubset(set2))
print("Set2 is subset of set1: ",set2.issubset(set1))
print("Set1 is superset of set2: ",set1.issuperset(set2))
print("Set2 is superset of set1: ",set2.issuperset(set1))
print("Set1 is disjoint of set2: ",set1.isdisjoint(set2))
print("Set1 is disjoint of set3: ",set1.isdisjoint(set3))
print("Set2 is disjoint of set3: ",set2.isdisjoint(set3))
'''

#6. POP-> RANDOMLY DELETES VALUE FROM SET
set3={9,0,7,8,9}
print("The original set is: ",set3)
print("The removed value is: ",set3.pop())
print("The set after poping value is: ",set3)
