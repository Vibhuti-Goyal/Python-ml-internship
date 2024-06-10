#STRINGS ARE IMMUTABLE-> NO MODIFICATION ALLOWED IN STRING 
"""

# SINGLE-LINE
str1="hello"
print(str1,end="\n")
print("\n")

#MULTI-LINE
str2= "hello" \
"all" \
"welcome"
print(str2)
print("\n")
str3='''hello
all welcome
strings'''
print(str3)
print("\n")

#SLICING
#[start_index:end_index:no_of_jumps]
str4="HELLLOOO EVERYONEE"
#-18/-17/-16/-15/-14/-13/-12/-11/-10/-9/-8/-7/-6/-5/-4/-3/-2/-1
print(str4[2:12:2])
print(str4[-13:-1])
#gives reversed string
print(str4[::-1])
print("\n")  

#STRING COMPARISON
s1="HELLO"
s2="hello"
print(s1==s2)
print(s1>s2)
print(s2>s1)

print(s1*2)
print(s1+s2)
print("\n")

str5="hello friends..."
print("frie" in str5)
print("s" in str5)
print("...." not in str5)
print("\n")

print(str5.upper())
print(s1.lower())
print("\n")

new_str=str5.replace("hello","hey")
print(new_str)
print(new_str.find("friends"))
print("\n")
print(str5.split())
str6="hey how, are, you, doing?"
print(str6.split(","))
print(str6.split(",",1))"""

#STRIP-> TO REMOVE SPACES
str7="      hellloo      heyyyy    "
print(str7.strip())
print(str7.lstrip())
print(str7.rstrip())
