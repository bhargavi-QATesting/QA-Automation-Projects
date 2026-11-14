from operator import index

fruits = ["apple", "banana", "cherry","orange","grapes","pomegranate"]
fruits[1] = "mosambi".upper()
fruits.append("pineapple")

print(fruits[::-1])
print(len(fruits))
print("chocolate" in fruits)
#print(fruits.sort())
print(fruits.count("cherry"))

for i in fruits:
    print(i)


#tuple
tuple(fruits)
print(tuple(fruits))

student = ["bhargavi"]
student.append("keerthi")
student.insert(0,"pushpa")
#student.remove("pushpa")
#print(student.sort())
#print(student.reverse())
#print(student.clear())
print(student.index("bhargavi"))

print(student)
for i in student:
    print(i)





