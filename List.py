#a.insert() - to insert elements in selective place
a=[1,2,3,4,5,6] #[0,1,2,3,4,5]
print(a)
a.insert(0,7)
print(a)
a.insert(2,5)
print(a)
print()

#a.append() - to insert element which automaticaly inserted at end of the list
a=[1,2,3]
a.append(5)
print(a)
print()

#a.pop() - to delete the element
a=[1,2,3,4]
a.pop(3) # I had selected third place to delete, which is number: 4
print(a)
print()

#a.extend() -  to merg the lists
a=[1,2,3,4]
b=[56,57,34]
a.extend(b)
print(a)
