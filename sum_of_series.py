
x=3
n= int(input("Enter 1st value: "))
n=abs(n)
ans=0

num=[]
while(n!=0):
   n=n-1
   ans=ans+x
   x=x*10+3
   
print(ans)

