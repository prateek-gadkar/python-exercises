# Exercise 3 - Personal Information Using Tuple
# Topics: tuples, indexing, negative indexing, slicing, len()

# --- Building the tuple from user input ---
name    = input("Enter name: ")
age     = int(input("Enter age: "))
course  = input("Enter course: ")
college = input("Enter college: ")
cgpa    = float(input("Enter CGPA: "))

info = (name, age, course, college, cgpa)   # a tuple: fixed, cannot be changed

# --- Display each element separately using indexing ---
print("\nElements by index:")
for i in range(len(info)):
    print(f"  info[{i}] = {info[i]}")

# --- The required operations ---
print("\nFirst element        :", info[0])    # counting starts at 0
print("Last element         :", info[-1])   # -1 always means the last item
print("First three elements :", info[0:3])  # slice: start included, stop EXCLUDED
print("Length of the tuple  :", len(info))
