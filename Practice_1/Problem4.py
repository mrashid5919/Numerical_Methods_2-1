length=input("Please enter the length of your password(minimum 8): ")
length=int(length)
p=""
p=p+'1'
p=p+'MR'
p=p+'@'
for i in range(length-4):
    p=p+(str(i%10))
print(p)