# Task 2: Sum of Integers from 1 to 50 using a loop.
#
# Problem Statement: Write a python program that
# 1.   Uses a for loop to iterate over numbers from 1 to 50.
# 2.   Calculates the sum of all integers in this range.
# 3.   Displays the final sum.


starting_number = int(input("Enter the starting number : "))
ending_number = int(input("Enter the ending number : "))
total = 0

for i in range(starting_number,ending_number+1):
    total = total + i

print("The sum of",starting_number,"to",ending_number,"is",total)
