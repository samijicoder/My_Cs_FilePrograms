# x = int(input('Enter the First Number: '))
# y = int(input('Enter the Second Number: '))
# variable3 = x
# x = y
# y = variable3
# print('The Value of x after swapping: {}'.format(x))
# print('The Value of y after swapping: {}'.format(y))
#
# x = int(input('Enter the height of Triangle in cms: '))
# y = int(input('Enter the Base of Triangle in cms: '))
# Area = 0.5*x*y
# print('Area of the described triangle is: ', Area,'cm square.')
#
# a=int(input("Enter the x2 Coefficient: "))
# b=int(input("Enter the x Coefficient: "))
# c=int(input("Enter the Constant term: "))
# d=(b*2)-(4*a*c)
# solution1=-1*b+d**0.5/2*a
# solution2=-1*b-d**0.5/2*a
# print('The two solutions are: ',solution1,'and',solution2)
#
# x = float(input('Enter the Temperature in Celsius: '))
# y = (x * 1.8) + 32
# print('Temperature on the Fahrenheit scale is: ',y)
#
# num = float(input("Enter a number: "))
# if num >= 0:
#    if num == 0:
#        print("Zero")
#    else:
#        print("Positive number")
# else:
#    print("Negative number")
#
# x = int(input('Enter the Year: '))
# if x % 4 == 0:
#     if x % 100 == 0:
#         if x % 400 == 0:
#             print(x, 'is a leap year.')
#         else:
#             print(x, 'is not a leap year.')
#     else:
#         print(x, 'is a leap year.')
# else:
#     print(x, 'is not a leap year.')
#
# num1 = float(input('Enter the First Number: '))
# num2 = float(input('Enter the Second Number: '))
# num3 = float(input('Enter the Third Number: '))
# if (num1 >= num2) and (num1 >= num3):
#     largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#     largest = num2
# else:
#     largest = num3
# print("The largest number is", largest)
#
# num = int(input('Enter the Number: '))
# sum = 0
# while(num>0):
#     remainder = num%10
#     sum = sum+remainder
#     num = num//10
# print('Sum of the digits of the given number is:', sum)
#
# num = int(input('Enter the Number: '))
# print(len(str(num)))
#
# sum1=0
# num=int(input("Enter a number:"))
# temp=num
# while(num):
#     i=1
#     f=1
#     r=num%10
#     while(i<=r):
#         f=f*i
#         i=i+1
#     sum1=sum1+f
#     num=num//10
# if(sum1==temp):
#     print("The number is a strong number.")
# else:
#     print("The number is not a strong number.")
#
#
# def gcd(a, b):
#     if a == 0:
#         return b
#     return gcd(b % a, a)
#
#
# def lcm(a, b):
#     return (a / gcd(a, b)) * b
#
#
# a = int(input('Enter the First Number: '))
# b = int(input('Enter the Second Number: '))
# print('LCM of', a, 'and', b, 'is', lcm(a, b))
#
#
# num = int(input("Enter a number: "))
#
# sum = 0
#
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10
#
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")
#
# num = int(input('Enter a Number: '))
#
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
#
# else:
#     print(num, "is not a prime number")
#
# num = int(input('Enter the number: '))
# factorial = 1
# if num < 0:
#    print("Go study some math, factorial does not exist for negative numbers!")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)
#
