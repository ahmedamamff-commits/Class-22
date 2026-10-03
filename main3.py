import array as arr

#create an array
array_num = arr.array("i", [1, 3, 5, 3, 7, 9, 3])
print("Original array:"+str(array_num))

#Count the occurences in the element
print("Number of occurences of the number 3 in the said array:"+str(array_num.count(3)))

#Reverse the array
array_num.reverse()
print("Reverse the order of the items in the array:")
print(str(array_num))