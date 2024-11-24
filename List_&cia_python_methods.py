print(" " )
# ---------------------------List--------------------------------------
print(" " * 20 + "---------List----------")
print(" " )

# ------------------------ 1- Append Method --------------------------------------
print(" " * 20 + "1- Append Method")
# Adds an item to the end of the list.
fruits = ['apple', 'banana']
fruits.append('cherry')
print("append():", fruits)  # ['apple', 'banana', 'cherry']

# ------------------------ 2- Extend Method --------------------------------------
print(" " * 20 + "2- Extend Method")
# Extends the list by adding elements from another iterable (e.g., list, tuple).
fruits.extend(['date', 'elderberry'])
print("extend():", fruits)  # ['apple', 'banana', 'cherry', 'date', 'elderberry']

# ------------------------ 3- Insert Method --------------------------------------
print(" " * 20 + "3- Insert Method")
# Inserts an item at a specified index.
fruits.insert(1, 'blueberry')
print("insert():", fruits)  # ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']

# ------------------------ 4- Remove Method --------------------------------------
print(" " * 20 + "4- Remove Method")
# Removes the first occurrence of a specified value from the list.
fruits.remove('banana')
print("remove():", fruits)  # ['apple', 'blueberry', 'cherry', 'date', 'elderberry']

# ------------------------ 5- Pop Method --------------------------------------
print(" " * 20 + "5- Pop Method")
# Removes and returns the item at a specified index (default is the last item).
popped = fruits.pop(2)
print("pop():", popped, "| List:", fruits)  # 'cherry' | ['apple', 'blueberry', 'date', 'elderberry']

# ------------------------ 6- Clear Method --------------------------------------
print(" " * 20 + "6- Clear Method")
# Removes all items from the list, leaving it empty.
fruits_copy = fruits.copy()
fruits_copy.clear()
print("clear():", fruits_copy)  # []

# ------------------------ 7- Index Method --------------------------------------
print(" " * 20 + "7- Index Method")
# Returns the index of the first occurrence of a specified value.
idx = fruits.index('date')
print("index():", idx)  # 2

# ------------------------ 8- Count Method --------------------------------------
print(" " * 20 + "8- Count Method")
# Counts how many times a specified value occurs in the list.
fruits.append('apple')
count = fruits.count('apple')
print("count():", count)  # 2

# ------------------------ 9- Sort Method --------------------------------------
print(" " * 20 + "9- Sort Method")
# Sorts the list in ascending (default) or descending order.
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print("sort():", numbers)  # [1, 1, 3, 4, 5]

numbers.sort(reverse=True)
print("sort(reverse=True):", numbers)  # [5, 4, 3, 1, 1]

# ------------------------ 10- Reverse Method --------------------------------------
print(" " * 20 + "10- Reverse Method")
# Reverses the elements of the list in place.
numbers.reverse()
print("reverse():", numbers)  # [1, 1, 3, 4, 5]

# ------------------------ 11- Copy Method --------------------------------------
print(" " * 20 + "11- Copy Method")
# Creates a shallow copy of the list.
fruits_copy = fruits.copy()
print("copy():", fruits_copy)  # ['apple', 'blueberry', 'date', 'elderberry', 'apple']

# ------------------------ 12- Length Function --------------------------------------
print(" " * 20 + "12- Length Function")
# Returns the number of items in the list.
print("len():", len(fruits))  # 5

# ------------------------ 13- List Comprehension --------------------------------------
print(" " * 20 + "13- List Comprehension")
# A concise way to create a new list by applying an expression to each element in an iterable.
squares = [x**2 for x in range(5)]
print("List comprehension:", squares)  # [0, 1, 4, 9, 16]

# ------------------------ 14- Delete Statement --------------------------------------
print(" " * 20 + "14- Delete Statement")
# Deletes an item or a slice from the list using the `del` statement.
del fruits[1]
print("del fruits[1]:", fruits)  # ['apple', 'date', 'elderberry', 'apple']

del fruits[:2]
print("del fruits[:2]:", fruits)  # ['elderberry', 'apple']

# ------------------------ 15- Max and Min Functions --------------------------------------
print(" " * 20 + "15- Max and Min Functions")
# Returns the largest or smallest element in the list.
numbers = [3, 1, 4, 1, 5]
print("max():", max(numbers))  # 5
print("min():", min(numbers))  # 1

# ------------------------ 16- Sum Function --------------------------------------
print(" " * 20 + "16- Sum Function")
# Returns the sum of all items in the list (numeric values only).
print("sum():", sum(numbers))  # 14

# ------------------------ 17- Enumerate Function --------------------------------------
print(" " * 20 + "17- Enumerate Function")
# Returns an enumerate object with index-value pairs for the list.
fruits = ['apple', 'banana']
for index, fruit in enumerate(fruits):
    print(index, fruit)  # 0 apple, 1 banana

# ------------------------ 18- Zip Function --------------------------------------
print(" " * 20 + "18- Zip Function")
# Combines multiple iterables (e.g., lists) into a list of tuples.
names = ['Alice', 'Bob']
scores = [85, 90]
result = list(zip(names, scores))
print("zip():", result)  # [('Alice', 85), ('Bob', 90)]

print(" " )
# ---------------------------Dictionary--------------------------------------
print(" " * 20 + "---------Dictionary----------")
print(" " )

# ------------------------ 1- Creating a Dictionary --------------------------------------
print(" " * 20 + "1- Creating a Dictionary")
# Creating a dictionary with key-value pairs.
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Dictionary:", person)

# ------------------------ 2- Accessing Values --------------------------------------
print(" " * 20 + "2- Accessing Values")
# Accessing values using keys.
print("Name:", person['name'])

# ------------------------ 3- Updating a Value --------------------------------------
print(" " * 20 + "3- Updating a Value")
# Updating the value associated with a key.
person['age'] = 31
print("Updated Dictionary:", person)

# ------------------------ 4- Adding a Key-Value Pair --------------------------------------
print(" " * 20 + "4- Adding a Key-Value Pair")
# Adding a new key-value pair.
person['profession'] = 'Engineer'
print("After Adding:", person)

# ------------------------ 5- Removing a Key-Value Pair --------------------------------------
print(" " * 20 + "5- Removing a Key-Value Pair")
# Removing a key-value pair using `del`.
del person['city']
print("After Removing:", person)

# ------------------------ 6- Using pop() --------------------------------------
print(" " * 20 + "6- Using pop()")
# Removing and returning a value using its key.
profession = person.pop('profession')
print("Popped Value:", profession, "| After pop:", person)

# ------------------------ 7- Using popitem() --------------------------------------
print(" " * 20 + "7- Using popitem()")
# Removing and returning the last inserted key-value pair.
last_item = person.popitem()
print("Popped Item:", last_item, "| After popitem:", person)

# ------------------------ 8- Checking Keys --------------------------------------
print(" " * 20 + "8- Checking Keys")
# Checking if a key exists in the dictionary.
print("'name' in person:", 'name' in person)
print("'city' in person:", 'city' in person)

# ------------------------ 9- Getting Keys, Values, and Items --------------------------------------
print(" " * 20 + "9- Getting Keys, Values, and Items")
# Getting all keys, values, and items as separate objects.
print("Keys:", person.keys())
print("Values:", person.values())
print("Items:", person.items())

# ------------------------ 10- Clearing a Dictionary --------------------------------------
print(" " * 20 + "10- Clearing a Dictionary")
# Removing all items from the dictionary.
person.clear()
print("After clear():", person)


print(" " )
# ---------------------------Set--------------------------------------
print(" " * 20 + "---------Set----------")
print(" " )

# ------------------------ 1- Creating a Set --------------------------------------
print(" " * 20 + "1- Creating a Set")
# Creating a set with unique values.
fruits = {'apple', 'banana', 'cherry'}
print("Set:", fruits)

# ------------------------ 2- Adding an Element --------------------------------------
print(" " * 20 + "2- Adding an Element")
# Adding a new element to the set.
fruits.add('date')
print("After add():", fruits)

# ------------------------ 3- Removing an Element --------------------------------------
print(" " * 20 + "3- Removing an Element")
# Removing an element using `remove()` (raises an error if not found).
fruits.remove('banana')
print("After remove():", fruits)

# ------------------------ 4- Using discard() --------------------------------------
print(" " * 20 + "4- Using discard()")
# Removing an element using `discard()` (no error if not found).
fruits.discard('banana')
print("After discard():", fruits)

# ------------------------ 5- Union of Sets --------------------------------------
print(" " * 20 + "5- Union of Sets")
# Combining two sets.
set1 = {'apple', 'banana'}
set2 = {'cherry', 'date'}
union_set = set1.union(set2)
print("Union:", union_set)

# ------------------------ 6- Intersection of Sets --------------------------------------
print(" " * 20 + "6- Intersection of Sets")
# Getting the common elements between sets.
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# ------------------------ 7- Difference of Sets --------------------------------------
print(" " * 20 + "7- Difference of Sets")
# Getting elements in one set but not in the other.
difference_set = set1.difference(set2)
print("Difference:", difference_set)

# ------------------------ 8- Symmetric Difference --------------------------------------
print(" " * 20 + "8- Symmetric Difference")
# Getting elements in either set but not in both.
symmetric_diff = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_diff)

# ------------------------ 9- Checking Subsets and Supersets --------------------------------------
print(" " * 20 + "9- Checking Subsets and Supersets")
# Checking if one set is a subset or superset of another.
print("set1 is subset of union_set:", set1.issubset(union_set))
print("union_set is superset of set1:", union_set.issuperset(set1))

# ------------------------ 10- Clearing a Set --------------------------------------
print(" " * 20 + "10- Clearing a Set")
# Removing all elements from the set.
fruits.clear()
print("After clear():", fruits)
