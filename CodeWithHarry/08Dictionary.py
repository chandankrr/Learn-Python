d1 = {}
# print(type(d1))

d2 = {"Chandan": "Chicken", 
      "Abhijeet": "Maggie",
      "Atul": {"B": "Maggie", "L": "Rice", "D": "Roti"}}

# Accessing dictionary
print(d2)
print(d2.get("Harry"))
print(d2["Chandan"])
print(d2["Atul"]["L"])

# adding
d2["Ravi"] = "Sandwich"
print(d2)
print(d2["Ravi"])

# deleting
del d2["Atul"]
print(d2)

# coping
# d3 = d2
# del d3["Chandan"] # d2 and d3 are pointing to same that's why same will take place after deleting
# print(d2)

d3 = d2.copy()
del d3["Chandan"]
print(d2)

# update
d2.update({"Payal": "Aloo paratha"})
print(d2)

# keys and items
print(d2.keys())
print(d2.items())