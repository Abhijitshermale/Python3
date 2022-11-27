# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("Input/Letters/starting_letter.txt") as data:
    str1 = data.read()

with open("Input/Names/invited_names.txt") as data1:
    str2 = data1.read().split()
for i in str2:
    str3 = str1.replace("[name]", i)
    print(str3.strip())
    print()
