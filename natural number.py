#sum of n natural number
num=int(input("enter the name:"))
if num<0:
  print("enter the number")
else:
  sum_numbers =0
  count=1
  while count<= num:
    sum_numbers+=count
  count+=1
  print("the sum of natural number is:",sum_numbers)
