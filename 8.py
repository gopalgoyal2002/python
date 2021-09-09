

a = int(input("Enter year value: "))
b = int(input("Enter month value: "))
c = int(input("Enter date value: "))


if((b>=0 and b<=12) and (c>=0 and c<=31)):
  print("this is valid")
else:
  print("this is not valid")