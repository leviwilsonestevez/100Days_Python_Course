#Given a number sum all is positions
number=input("Type a integer number\n")
sum=0
for digit in number:
    sum=sum+int(digit)
print("The sum of the digits from the inserted number is : "+str(sum))
