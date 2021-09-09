
x=0
a = int(input("Enter 1st value: "))
a=abs(a)
b=a
sum=0
while(a!=0):
   
   x=int(a%10)
   
   sum+=int(x*x*x)
   a=int(a/10)

if(int(sum)==b):
  print("this is a amstrong number")
else:
  print("this is a not amstrong number")