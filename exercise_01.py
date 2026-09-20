# Exercise 1 - Student Details
# Topics: input(), data types (str, int, float, bool), formatted output

# --- Reading the details ---
# input() ALWAYS returns a string, so we wrap it in int()/float()
# when we need a number.
name      = input("Enter name: ")                            # string
age       = int(input("Enter age: "))                        # integer
cgpa      = float(input("Enter CGPA: "))                     # float
gender    = input("Enter gender: ")                          # string

# A Boolean is made by asking a question that is True or False:
# "yes" == "yes" -> True,  "no" == "yes" -> False
hosteller = input("Is the student a hosteller? (yes/no): ").lower() == "yes"

roll      = int(input("Enter roll number: "))                # integer

# --- Displaying in a well-formatted way ---
print()
print("-------------------------------")
print("        STUDENT DETAILS        ")
print("-------------------------------")
print(f"Name      : {name}")
print(f"Roll No.  : {roll}")
print(f"Age       : {age}")
print(f"Gender    : {gender}")
print(f"CGPA      : {cgpa}")
print(f"Hosteller : {hosteller}")
print("-------------------------------")

# Bonus: prove each value really has the right data type
print("\nData types:")
print("  name      ->", type(name))
print("  roll      ->", type(roll))
print("  age       ->", type(age))
print("  gender    ->", type(gender))
print("  cgpa      ->", type(cgpa))
print("  hosteller ->", type(hosteller))
