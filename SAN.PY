#Check whether a Given Number is even or odd one
# n=int(input("Enter any number : "))
# if n%2==0:
#     print(f"{n} is Even number")
# else:
#     print(f"{n} is Odd number")

#check if number is positive or negative
# n=int(input("Enter Number : "))
# if n>0:
#     print(f"{n} number is positive")
# elif n==0:
#     print("Zero")
# else:
#     print(f"{n} IS Negative number")

# #ODD NUMBER IN RANGE
# n=int(input("Enter Range ! : "))
# for i in range(n):
#     if i % 2 !=0:
#         print(i)

#Check number is paliandrome in range
# m=int(input("Enter the range : "))
# temp=m
# rev=0
# while(m>0):
#     dig=m%10
#     rev=rev*10+dig
#     m=m//10
# if(temp==rev):
#     print("is palindrome")
# else:
#     print("is not paliandrome")

# def paliandrome(n):
#     return str(n)=="".join(reversed(str(n)))
# n=int(input("Enter Number : "))
# if paliandrome(n):
#     print("IS Paliandrome")
# else:
#     print("Isn t paliandrome")

#reverse number
# n=int(input("Enter number"))
# temp=n
# rev =0
# while(n>0):
#     d=n%10
#     rev=rev*10 +d
#     n=n//10
# print(rev)

#All number that are not Divisible by either 2 or 3
# n=int(input("Enter range !: "))
# for i in range(n):
#     if i%2 !=0 and i%3 !=0:
#         print(i)


# n=int(input("Enter the renge : "))
# k=int(input("Enter Divisible : "))
# for i in range(n+1):
#     if i%k==0:
#         print(i)

#sum of Digits of number
# n=int(input("Enter number : "))
# tot=0
# while(n>0):
#     dig=n%10
#     tot=tot+dig
#     n=n//10
# print(f"Sum of DIGIT OF Number is:{tot}")

#Count number of digits

# n=int(input("Enter number : "))
# str(n)
# m=list(str(n))
# print(len(str(n)))

#Divisor of any number
# n=int(input("Enter number : "))
# for i in range(1,n+1):
#     if (n%i==0):
#         print(i)

#smallest divisor of integer
# l=[]
# n=int(input("Enter number : "))
# for i in range(1,n+1):
#     if(n%i==0):
#         l.append(i)
# print(l[1])

#Binary Equivalent of an integer using recursion
# l=[]
# def binary(b):
#     if(b==0):
#         return 1
#     dig=b%2
#     l.append(dig)
#     binary(b//2)
# n=int(input("Enter number : "))
# binary(n)
# l.reverse()
# for i in l:
#     print(i) 
# #print(i)
    
# try:
#     n=int(input("Enter marks:"))
#     if n==100 and n>=90:
#         print("Genius")
#     elif n<90 and n>=80:
#         print("Excellent")
#     elif n<80 and n>=70:
#         print("Good")
#     elif n<70 and n>=50:
#         print("Work hard")
#     elif n<50 and n>=0:
#         print("fail")
#     elif n>100 or n<0:
#         print("Out of range")
# except ValueError:
#     print("Invalid input")

# quadratic equation
print("Equation : ax^2 + bx + c = d")
r=int(input("Enter a :"))
k=int(input("Enter b :"))
f=int(input("Enter c :"))
m=int(input("Enter d :"))
print(f"{r}x^2 +{k}x + {f} = {m}")
d=f-m
print(f"{r}x^2 + {k}x + {d} = 0")
d=k**2 -4*r*d
print("Formula of delta : b^2 - 4ac")
if d>0:
    t=d**0.5
    print(f"delta is : {d} \nThen")
    print(f"t1= +{round(t,2)}\nt2= -{round(t,2)}")
    print(f"solve for x1 and x2\n")
    x1=(-k+t)/(2*r)
    x2=(-k-t)/(2*r)
    print(f"solution is x1 = {round(x1,2)} and x2 = {round(x2,2)}")
    print("\nYou can verify you self ")
elif d==0:
    print(f"delta is : {d}\nMeans")
    print("x1 is equal to x2\n x1=x2")
    u=-k/2*r
    print(f"print x1=x2=:{round(u,2)}")
    print("You can verify you self")
else:
    print(f"\ndelta is :{d}\nSo")
    print("\nTry complex number")