#Check whether a Given Number is even or odd 
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
n=int(input("Enter number : "))
for i in range(1,n+1):
    if (n%i==0):
        print(i)

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
    
