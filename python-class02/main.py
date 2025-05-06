Muskan = 10
Ali = 5
print("Arithmetic Operators:")
print(Muskan + Ali)  # Addition
print(Muskan - Ali)  # Subtraction
print(Muskan * Ali)  # Multiplication
print(Muskan / Ali)  # Division
print(Muskan // Ali) # Floor Division
print(Muskan % Ali)  # Modulus
print(Muskan ** Ali) # Exponentiation
print()

# Assignment Operators
A = 5
print("Assignment Operators:")
A += 3  # A = A + 3
print(A)
A -= 2  # A = A - 2
print(A)
A *= 4  # A = A * 4
print(A)
A /= 6  # A = A / 6
print(A)
A %= 3  # A = A % 3
print(A)
A **= 2 # A = A ** 2
print(A)
print()

# Comparison Operators
print("Comparison Operators:")
print(Muskan == Ali)  # Equal to
print(Muskan != Ali)  # Not equal to
print(Muskan > Ali)   # Greater than
print(Muskan < Ali)   # Less than
print(Muskan >= Ali)  # Greater than or equal to
print(Muskan <= Ali)  # Less than or equal to
print()

# Logical Operators
A = 5
B = 10
print("Logical Operators:")
print(A > 3 and B < 15)  # and operator
print(A < 3 or B > 5)    # or operator
print(not(A > 3))        # not operator
print()

# Identity Operators
A = [1, 2, 3]
B = [1, 2, 3]
C = A
print("Identity Operators:")
print(A is B)  # is operator (checks if A and B refer to the same object)
print(A is not B)  # is not operator (checks if A and B do not refer to the same object)
print(A is C)  # Checks if A and C are the same object
print()

# Membership Operators
list_ = [1, 2, 3, 4]
print("Membership Operators:")
print(3 in list_)  # in operator
print(5 in list_)  # in operator
print(3 not in list_)  # not in operator
print(5 not in list_)  # not in operator
print()

# Bitwise Operators
Muskan = 10  # 1010 in binary
Ali = 4   # 0100 in binary
print("Bitwise Operators:")
print(Muskan & Ali)  # AND operator
print(Muskan | Ali)  # OR operator
print(Muskan ^ Ali)  # XOR operator
print(~Muskan)     # NOT operator
print(Muskan << 1) # Left shift operator
print(Muskan >> 1) # Right shift operator

