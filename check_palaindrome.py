
x=0
a = int(input("Enter 1st value: "))
a=abs(a)
b=a

num=[]
while(a!=0):
   
   x=int(a%10)
   
   num.append(x)
   a=int(a/10)

j=len(num)-1
i=0
while(i<j):
    if(num[i]!=num[j]):
       print("this is not a palindrome")
       exit(0)
    j=j-1
    i=i+1   
print("this is  a palindrome")