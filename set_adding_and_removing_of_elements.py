# ADDING AND REMOVING SET ELEMENTS


# add(x) -> adds a new element
names ={"Kesh", "Daniel", "Uche", "Achilihu", "David", "Kesh", "Daniel"}
names11 = names.add("Oluwa")
print(names)



# remove(x) -> removes x, raises an error if missing
names2 ={"Kesh", "Daniel", "Uche", "Achilihu", "David", "Kesh", "Daniel"}
names22 = names2.remove("Oluwa")
print(names2)


names3 ={"Kesh", "Daniel", "Uche", "Achilihu", "David", "Kesh", "Daniel"}
names33 = names3.remove("Kesh")
print(names3)




# discard(x) -> removes x, does nothing if missing (safer)
names4 ={"Kesh", "Daniel", "Uche", "Achilihu", "David", "Kesh", "Daniel"}
names44 = names4.discard("Oluwa")
print(names4)


names5 ={"Kesh", "Daniel", "Uche", "Achilihu", "David", "Kesh", "Daniel"}
names55 = names5.discard("Daniel")
print(names5)



# clear() -> removes all elements
names6 ={"Kesh", "Daniel", "Uche", "Achilihu", "David", "Kesh", "Daniel"}
name66 = names6.clear()
print(names6)