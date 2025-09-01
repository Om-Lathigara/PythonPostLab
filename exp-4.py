#creating a list
fruits = ["apple", "banana", "cherry"]
print("Initial fruits list:", fruits)
#creating list 2
vegetables = ["carrot", "broccoli", "spinach"]
print("Initial vegetables list:", vegetables)
#appending both lists
fruits.append(vegetables)
print("\nFruits list after appending vegetables:", fruits)
print("Accessing nested vegetable 'broccoli':", fruits[-1][1])

#sum
List = [1, 2, 3, 4, 5]
print(sum(List))

List = ['gfg', 'abc', 3]
print(sum(List))

#count
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.count(1))

#length
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(len(List))

#index function
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.index(2))
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.index(1, 3))

#min method
#Calculates min of all the elements of List.
numbers = [5, 2, 8, 1, 9]
print(min(numbers))

#max method
#Calculates the maximum of all the elements of the List.
numbers = [5, 2, 8, 1, 9]
print(max(numbers))

#sort method
List = [2.3,4.445,3,5.33,1.054,2.5]
List.sort()
print(List)

