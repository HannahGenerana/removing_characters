# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

# pseudocode

# create a function for the words and length of the n to be remove
def removing_letters (random_words, length):

# print the word before removing characters
    print ("The word is", random_words)

# create a variable that will remove n characters from the word
    remove = random_words [length:]

# return the new word
    return remove

# print the word with remove characters
print ("Characters will now be remove from the word")

print (removing_letters("Technology and Science", 5))
print (removing_letters("Computer Engineering", 10))