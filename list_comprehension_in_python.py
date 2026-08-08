# LIST COMPREHENSION


# Building a list of squares the traditional way needs a loop and append():
squares = []
for i in range(1, 6):
    squares.append(i * i)
print (squares)


# List Comprehension does it in one line:
squares = [x*x for x in range(1, 7)]
print (squares)
# [1, 4, 9, 16, 25,36]


doubled = [n*2 for n in [1,7,11,25]]     # jersey numbers doubled
print (doubled)


players = ["kesh, david, ronaldo, messi"]
upper = [p.upper() for p in players]     # WITH condition:
print (upper)


even = [x for x in range(1,11) if x % 2 == 0]
print (even)
