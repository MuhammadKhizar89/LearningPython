# print("Hi");
# a=complex(8,2)
# print (a)
#mutable ->Changes---->List

#immutable ->Doesn't--->tuple

# dictionary->key and value (objects in javascript)

# **->power 2**4 =16  2power4=16
# //->floor division 8//5=1

#Simple Calculator
# by default it takes string

# num1=input("Enter Number:");
# num2=input("Enter Number:");
# print("Addition",int(num1)+int(num2));

# num1=int(input("Enter Number:"));
# num2=int(input("Enter Number:"));
# print("Addition",num1+num2);

# abc="hello" 
# new=abc[0:2] # 2 index sy peechy peechy
# print (new)

# srtipp="!!!hellom!1!2!!"
# print(srtipp.lstrip("!"))
# print(srtipp.rstrip("!"))
# print(srtipp.strip("!"))
# i = "shery"
# for k in range(len(i)):
#     print(i[k])



# # List
# Marks=[2,3,"wq"]
# print (Marks);

# if(Marks[2]=="wq"):
#     print("wq")

# if 2 in Marks:
#     print("Present")

# if "w" in "wq":
#     print("Present");    

# print(Marks[0:4:2]); #staring,ending,skip

# list=[i*i for i in range(10) if i%2==0]
# print(list);

# list.append(5);
# print(list);
# list.sort();
# print(list);
# list.sort(reverse=True);
# print(list);
# list.pop();
# # print(list.index(0));
# # print(list);
# print(list.index(64)); # yani 64 kon sy index pr pra hy
# print(list.count(5));
# m=list;
# m[0]=32;
# print(list)
# # m make changes in list so we use
# m=list.copy();
# m[0]=2;
# print(list)
# list.insert(1,78)#1 index pr 78
# print(list)
# list.extend(m);
# print(list)
# k=list+m;
# print(k);
# print(list)

# Tuple
tup=(1,2,"hehe")
print(tup);
if 2 in tup:
    print("Present")

# slicing krny kay baad new tuple return hoga previous change ni hoga
tup2=tup[0:2];
print(tup2);
# We can cancatinate two tuples
print(tup.count(3));
print(tup.index(1,0,2)); #tofind,starting index,ending index
# to change tuple convert it into list
# Define a tuple
GFG_tuple = (1, 2, 3)
 
# Convert the tuple to a list for changing
GFG_list = list(GFG_tuple)
GFG_list.append(2);
print(GFG_list)
GFG_tuple=tuple(GFG_list);
print(GFG_tuple)

# fString
a="hello"
b="world"
print(f"({a} hehe {b})");
# or old tradition (a.format(b))
letter="My Name is{} and I am {} years old"
age="18"
name="abc"
print(letter.format(name,age));
# format can do more things like floating will be upto 2 decimal

# DocString
def square(n):
    '''Return the square of a number'''
    return n**2
print(square(5));

print(square.__doc__)#It returns the docstring means comment of the function
# To document our code Only work after defination of function

#Recursion
def fab(n):
    if(n==0):
        return 0;
    if(n==1):
        return 1;
    return fab(n-1)+fab(n-2);

for a in range(6):
 print(fab(a));

#  Sets
s={1,2,3,3,"hello","hello"}
print(s);
# No gaurantee of order
ab=set(); #to make empty set if we do this{} then first it thinks it is dictionary
print(type(s),type(ab))

for value in s:
    print(value);
s2={"hello","World"}
print(s.union(s2));
print(s);
s.update(s2);
print(s);
s.intersection_update(s2); #update will the orignal one
print(s)
s.symmetric_difference(s2);# for values that are not comn in each others
