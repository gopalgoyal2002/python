
x=0
a = int(input("Enter 1st value: "))
a=abs(a)
while(a!=0):
   
   x=x+a%10
   a=int(a/10)

print(int(x))