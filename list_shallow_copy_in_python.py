# LIST COPY () AND SHALLOW COPY()

list1 = [10, 20]

# Without copy(), two variables can accidentally point to the SAME list.
list2 = list1                # same list! changing list2 changes list1 too
list2.append(30)      

print (list1)
print (list2)


# copy() creates a brand new list object:
list4 = [50, 60]      
list3 = list4.copy()             # list3 is now independent

list3.append(70)      
print (list3)
print (list4)
