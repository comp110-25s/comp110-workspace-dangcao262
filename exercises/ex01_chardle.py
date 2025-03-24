"""EX01 - Chardle - a cute step toward Wordle."""

__author__ = "730747262"


user_name = input("Good day baka! What's your name? ")


print("Hello " + user_name + "-chan! ")


first_word = input("Enter a five-character word! ")
first_letter = input("Enter a single character too! ")

index_i = 0

print("Searching for " + first_letter + " in " + first_word + "!")


"""use for-loop"""
for x in first_word:
    index_i = index_i + 1
    if x == first_letter:
        index = str(index_i)
        print(first_letter + " is found at " + index)
else:
    print("That letter is not found.")
