# REMOVING ELEMENTS TO A LIST

fruits = ["apple", "banana", "cherry", "mango","coconut", "cherry"]

# remove(value)-> removes the first matching value
fruits.remove("cherry")
print (fruits)


# pop(index)-> removes & returns the element at that index (last, if no index given)
fruits2 = ["apple", "banana", "cherry", "mango", "lime"]
fruits2.pop(3)
print (fruits2)


# clear()-> empties the entire list
fruits3 = ["apple", "banana", "cherry", "mango", "grape"]
fruits3.clear()
print (fruits3)


# del list[i] -> deletes an elementt
fruits4 =["apple", "banana", "cherry", "mango", "pineapple" ]

del fruits4 [2]
print (fruits4)

# del list[i] -> deletes a slice
fruits5 =["apple", "banana", "cherry", "mango", "pineapple","lime" ]

del fruits5 [2:6]
print (fruits5)

# del list[i] -> deletes entire list
del fruits4