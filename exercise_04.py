# Exercise 4 - String Analysis
# Topics: string methods, indexing, the `in` operator

sentence = input("Enter a sentence: ")

# --- Character and space counts ---
print("\nNumber of characters:", len(sentence))
print("Number of spaces    :", sentence.count(" "))

# --- Case conversion (returns a NEW string; the original stays unchanged) ---
print("Uppercase           :", sentence.upper())
print("Lowercase           :", sentence.lower())

# --- First and last character ---
print("First character     :", sentence[0])
print("Last character      :", sentence[-1])

# --- Word search ---
word = input("\nEnter a word to search for: ")
if word in sentence:                        # `in` checks whether word is inside sentence
    print(f"Yes, '{word}' exists in the sentence.")
else:
    print(f"No, '{word}' does not exist in the sentence.")

# Tip: for a case-insensitive search use:
# if word.lower() in sentence.lower():
