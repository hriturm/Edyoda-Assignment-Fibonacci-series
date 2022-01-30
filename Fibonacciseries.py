num=int(input("Enter the maximum number to print Fibonacci Series"))
n1=0
n2=1
sum=0
if num<=0:
    print("Please enter the number greater than zero")
else:
    for i in range(0,num):
        print(sum)
        n1=n2
        n2=sum
        sum=n1+n2