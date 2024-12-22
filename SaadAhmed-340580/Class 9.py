# Program to print sequences using while loops
# a. First 10 Even numbers
even_count = 1
even_number = 2
print("First 10 Even Numbers:")
while even_count <= 10:
    print(even_number, end=" ")
    even_number += 2
    even_count += 1
print("\n")
# b. First 10 Odd numbers
odd_count = 1
odd_number = 1
print("First 10 Odd Numbers:")
while odd_count <= 10:
    print(odd_number, end=" ")
    odd_number += 2
    odd_count += 1
print("\n")
# c. First 10 Natural numbers
natural_count = 1
print("First 10 Natural Numbers:")
while natural_count <= 10:
    print(natural_count, end=" ")
    natural_count += 1
print("\n")
# d. First 10 Whole numbers
whole_count = 0
print("First 10 Whole Numbers:")
while whole_count < 10:
    print(whole_count, end=" ")
    whole_count += 1
print("\n")