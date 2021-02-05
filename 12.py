#The location of the file is determined by the user.
location = input("State the location of the text file to be read: ")

#Open the file the user specifies.
f = open(location, 'r')
textfile = f.read()
f.close()

#For every char in the original text, use the formula to get its mirrored ascii char.
mirrored_ascii = ""

for letter in textfile:
    mirrored_ascii += (chr(128 - ord(letter)))

#Output the results.
print("Original Text: \n" + textfile + "\n")
print("Original Text (Reversed): \n" + textfile[::-1] + "\n")

print("Text With Mirrored Ascii Chars: \n" + mirrored_ascii + "\n")
print("Text With Mirrored Ascii Chars (Reversed): \n" + mirrored_ascii[::-1])