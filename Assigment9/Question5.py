#Write a python script to print first N odd natural numbers in reverse order
n=int(input("enter a number: "))
i=n-1
while i>=1:
    print(i,end=' ')
    i-=2
