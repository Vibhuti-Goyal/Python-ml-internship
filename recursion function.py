'''def fun_rec(num):
    if (num==0) or (num ==1):
        return 1
    elif num<0:
        print("Factorial of negative number can not be calculated")
        return 0
    else:
        return(num*fun_rec(num-1))
    
num=int(input("Enter the number: "))
result=fun_rec(num)
print(f"The factorial of {num} is:",result)

#variable scope-region where we can access the value
#lifetime-the number of lines of code till variable can be used

#LOCAL VARIABLE
def loc_var():
    r="This is variable inside function"
    print("The result is: ",r)

loc_var()
#print("The result is: ",r)-> gives error because r is local variable

#GLOBAL VARIABLE
gv="This variable is outside the function"
def glo_var():
    print("The result is: ",gv)
glo_var()
print("The result is: ",gv) #donot show error because variable is global

#NON-LOCAL VARIABLE
ro="hey" #global for out_fun()
def out_fun():
    ro="This is outside of the function" #local for out_fun() and global for in_fun() 
    print("The first function: ",ro)

    def in_fun():
        ro="This is inner of function" #non local variable
        print("The second function: ",ro)
    in_fun()

out_fun()
print("the global variable value is: ",ro)

try:
    num1=int(input("Enter numerator: "))
    num2=int(input("Enter denominator: "))
    result=num1/num2
    print("The result is: ",result)
    list1=[1,2,3,4,5]
    print(list1)
    i=int(input("Enter the index: "))    
    print("The element of list is: ",list1[i])

except ZeroDivisionError:
    print("can not divide a number by zero")
except IndexError:
    print("Index out of range")
else:
    print("No error ocuured!")
finally:
    print("This is finally block")


class Invalidage(Exception):
    pass

try:
    age=int(input("Enter age: "))
    if age<60:
        raise Invalidage()
    else:
        print("Valid age! Pension should be given")

except:
    print("Invalid age! No pension should be given")

'''
class Invalidage(Exception):
    pass


age=int(input("Enter age: "))
if age<60:
    print("Invalid age! No pension should be given")
    raise Invalidage()

else:
    print("Valid age! Pension should be given")


    

