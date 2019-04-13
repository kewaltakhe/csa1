a=int(input("enter the first_number:"))
b=int(input("enter the second_number:"))
option=input("enter 1 for addition:\nenter 2 for subtraction:\n")
#the sum
s=0
if option=="1":
   c=m=0
elif option=="2":
   c=m=1
else:
   print("option error")
  
#this program is an imitation of 4-bit adder-subtractor:

for p,k in zip(range(8),[1,2,4,8,16,32,64,128]):
    a_i=(a&k)>>p
    b_i=((b&k)>>p)^m
    s_i=a_i^(b_i)^c
    s=s|(s_i<<p)
    c=(a_i&b_i)|((a_i^b_i)&c)
    

print("sum=",s)
print("carry=",c)
