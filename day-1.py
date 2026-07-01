# Write a program to check whether a number is positive, negative, or zero using if-elif-else.
# Use a for loop to print the multiplication table of 7.
# Use a while loop to print numbers from 10 down to 1.
# Print numbers from 1 to 10, but skip 5 using continue.
# Print numbers from 1 to 10, but stop when the number becomes 8 using break.

#1.
a=2
if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")

print("-------------------------")

#2.
for i in range(1,11):
    print("7*", i, " = ",i*7)

print("--------------------------")

#3.
a=10
while a>=1:
    print(a)
    a-=1

print("---------------------------")

#4.
for i in range(1, 11):

    if i == 5:
        continue

    print(i)

print("---------------------------")

#5.
for i in range(1, 11):

    if i == 8:
        break

    print(i)
