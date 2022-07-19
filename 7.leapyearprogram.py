n = input("enter the year: ")
year = int(n)
if (year%400 == 0):
  print("it is the leap year")
elif (year%100 == 0):
  print("it is not the leap year")
elif (year%4 == 0):
  print("it is the leap year")
else:
  print("it is not the leap year")
  