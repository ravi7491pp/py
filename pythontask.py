#to print the sum of all numbers between m and n (both included)
m = int(input("Enter the starting number"))
n = int(input("Enter the ending number"))

sum = 0
for i in range(m, n + 1):
    sum = sum+i
print("The Sum Is", sum)

#check if number is perfectly divides the others
a = int(input("Enter The First Number: "))
b = int(input("Enter The Second Number: "))

if a%b == 0:
    print("a is divisible by b")
elif b%a==0: 
    print("b is divisible by a")
else:
    print("neither a Is divisible by b nor b is divible by a")

# to print the factorial of the given number
f = int(input("Enter The Number For Factorial "))
factorial = 1
for i in range(1,f+1):
      factorial = factorial*i  

print("The Factorial Is", factorial)


# to print the area and perimeter of a circle if the diameter is given
import math
d = int(input("Enter The Diameter "))
r = d/2
perimeter = 2*math.pi*r
area = math.pi*r**2

print("The Perimeter of circle is: ",perimeter)
print("The Area of the circle is: ",area)

# print the given pattern
m = int(input("Enter The Number"))
for i in range(1,m+1):
    for j in range(1,i+1):
        print(j, end="")
    print()
