

a = int(input("Enter 1st value: "))
b = int(input("Enter 2st value: "))
c = int(input("Enter 3st value: "))


if(a==b and b==c):
  print("this is equilateral")
elif (a==b or a==c or c==a):
  print("this is isosceles")
else:
  print("this is scalene")