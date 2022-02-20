grocery = ["Harpic", "Vim", "Tide", "Apple", 100, "Kitkat"]
print(grocery)
print(grocery[5])

numbers = [10, 2, 31, 89, 0, 52]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers[::-1])
print(numbers[1:4])

print(min(numbers))
print(max(numbers))

numbers.append(10)
print(numbers)

numbers.insert(2, 1000)
print(numbers)

numbers.remove(0)
print(numbers)

numbers.pop()
print(numbers)

numbers[0] = 500
print(numbers)
