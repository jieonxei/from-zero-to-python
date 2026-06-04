# Exercise 10
# Finding Extreme (Min/Max) in a list
# Given a list of integers, find and print both the largest and the smallest numbers.

nums = [45, 2, 89, 12, 7]

largest = max(nums)
smallest = min(nums)

print(f"Largest: {largest}")
print(f"Smallest: {smallest}")

# max(nums): Internally, this function assumes the first element is the largest, then compares it against every other element in the list, updating the “current winner” as it goes.
# min(nums): Works identically to max, but tracks the lowest value found.
