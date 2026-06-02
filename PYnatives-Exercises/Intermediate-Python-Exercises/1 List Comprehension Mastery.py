# List Comprehension Mastery
# Exercise 1
# Write a single-line list comprehension that takes a list of strings, 
# filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.


words = ["apple", "bat", "cherry", "dog", "elderberry", "starapple"]

filtered = [w.upper() for w in words if len (w) >=4 ]

print(f"Original Array {words}")
print(f"filtered result {filtered}")


# the "for w in words" iterates through each element in the original list
# the "if len(w) >=4" allowing 4 strings up to pass the expression phase
# the "w.upper" this transform the items that passes the filter into new brandlist