s = input("What is your name?")
print(s,"has ",len(s),"letters")
print("The first letter is ",s[0])
print("The last letter is ",s[-1])
print("The first three letters are ",s[0:3])
print("The last three letters are ",s[-3:])
print("Uppercase: ",s.upper())
print("Lowercase: ",s.lower())
print("Title case: ",s.title())
#what is title case?
# Title case is a style of writing where the first letter of each word is capitalized, while the rest of the letters are in lowercase.
print("Swapcase: ",s.swapcase())
print("Reversed: ",s[::-1])
print("Capitalized: ",s.capitalize())
print("Is alphanumeric: ",s.isalnum())
print("Is alphabetic: ",s.isalpha())
print("Is digit: ",s.isdigit())
statement  = "raj, ram, rajesh  are selected for the job"
if s in statement:
    print(s,"has been selected for the job")
else:
    print(s,"has not been selected for the job")

print(s)
print("The number of times 'raj' appears in the statement is: ",statement.count("raj"))
dict = {97:69}
text = "Hello ram"
print(text)
print(text.translate(dict))
print("Count of 'a' in text:", text.count("a"))
print("Index of 'a' in text:", text.index("a"))
print("Find 'a' in text:", text.find("a"))
print("Find 'z' in text:", text.find("z")) #returns -1 if not found
print("Replace 'ram' with 'raj':", text.replace("ram", "raj"))
print("Split text:", text.split())
print("Split text with comma:", text.split(","))
print("Join text with comma:", ",".join(text))
print("Join text with space:", " ".join(text))
print("Join text with hyphen:", "-".join(text))
print("Join text with underscore:", "_".join(text))

# 🔢 48–57: Digits

# 48: 0   49: 1   50: 2   51: 3   52: 4
# 53: 5   54: 6   55: 7   56: 8   57: 9

# 🔤 65–90: Uppercase Letters (A-Z)

# 65: A   66: B   67: C   ...   90: Z

# 🔡 97–122: Lowercase Letters (a-z)

# 97: a   98: b   99: c   ...   122: z