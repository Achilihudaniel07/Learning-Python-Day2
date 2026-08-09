#  SET OPERATORS

names = {"Kesh", "Daniel", "Uche", "Achilihu", "David", "Kesh", "Daniel"}
names2 = {"David", "Michael", "Samuel", "Peter", "Kesh"}

# Union ( | ) ->  everything from both sets
print (names | names2)


# Intersection ( & ) ->  only the common elements
print (names & names2)


# Difference ( - )  ->  in the first set, but not the second
print (names - names2)
print (names2 - names)



# Symmetric Difference ( ^ ) ->  everything except what's common
print (names ^ names2)
