mystr = "chandan is a good boy"
print(mystr[0:7])  # 0 -> include but 7 -> excluded
print(len(mystr))

# print(mystr[78])  # give error
print(mystr[0:78])
print(mystr[0:7:2])

print(mystr[-21:])
print(mystr[::-1])

print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith("boy"))
print(mystr.count("o"))
print(mystr.find("is"))
print(mystr.lower())
print(mystr.upper())
print(mystr.capitalize())
print(mystr.replace("is", "are"))