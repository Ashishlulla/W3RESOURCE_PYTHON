# 4.Write a Python program to get a string
# from a given string where all occurrences of its first char
# have been changed to '$', except the first char itself.

a = "restart"
for i in a[1:]:
    if i == a[0]:
        b = a[1:].replace(i, "$")

print(a[0]+b)

# 5.Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.

a, b= "abc", "xyz"
print(b[:2]+a[2:], a[:2]+b[2:])


# 6.Write a Python program to add 'ing' at the end of a given string 
# (length should be at least 3). If the given string already ends 
# with 'ing' then add 'ly' instead. If the string length of the
# given string is less than 3, leave it unchanged.

a = "abc"
if len(a) >= 3:
    if a.endswith("ing"):
        print(a+"ly")
    else:
        print(a+"ing")
else:
    print(a)
   
