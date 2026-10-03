#Different types of sets in Python
#Set of integars
my_set = {1, 2, 3}
print(my_set)

#set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

#Set cannot contain duplicate elements
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

#We can create a set from a list
my_set = set([1, 2, 3, 2])
print(my_set)

#Remove a number from a set
num_set = set([0, 1, 2, 3, 4, 5])
print(num_set)
num_set.pop()
print("After receiving the first element from the said set:")
print(num_set, "\n")