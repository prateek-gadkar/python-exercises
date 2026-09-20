# Exercise 2 - Student Marks Analysis
# Topics: lists, for loops, built-in functions sum()/max()/min()/len()

# --- Reading marks into a list ---
n = int(input("How many subjects? "))

marks = []                                    # start with an empty list
for i in range(n):                            # repeat n times
    m = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(m)                           # add the mark to the list

# --- Calculations using list functions ---
total   = sum(marks)                          # adds everything up
average = round(total / len(marks), 2)        # len() = number of items
highest = max(marks)
lowest  = min(marks)

# Count subjects with marks > 80 using our own loop
above_80 = 0
for m in marks:
    if m > 80:
        above_80 += 1
# (one-line alternative: above_80 = len([m for m in marks if m > 80]))

# --- Displaying the results ---
print("\nMarks entered     :", marks)
print("Total marks       :", total)
print("Average marks     :", average)
print("Highest mark      :", highest)
print("Lowest mark       :", lowest)
print("Subjects above 80 :", above_80)
