# Exercise 1 — Even or odd

# Take a number from the user and determine whether it is even or odd using the modulus operator.



# Exercise 2 — Largest number

# Take three numbers and find the largest using if, elif and else.



# Exercise 3 — Sum of numbers

# Use a for loop and range() to calculate the sum of numbers from 1 to 100.






number = int(input("Enter a number: "))

if number%2==0:
    print("even")
else:
    print("odd")



num = [1,5,3]


if num[0]>num[1] and num[0]>num[2]:
    print(num[0])
elif num[1]>num[0] and num[1]>num[2]:
    print(num[1])
else:
    print(num[2])

sum=0
for i in range(1,101):
    print(i)
    sum+=i
    print(sum)

