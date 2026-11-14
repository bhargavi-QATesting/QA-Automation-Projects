# reverse a number
number = 5864
reversed_number = 0

while number!=0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10
print(reversed_number)

# reverse a string
text = "Python"
print(text[::-1])

#without list comprehension
even_num = []
for i in range(1,11):
    if i % 2 == 0:
        even_num.append(i)
print(even_num)

squares = []
for i  in range(1,6):
     squares.append(i*i)
print(squares)

#list comprehension
even_num = [i for i in range(1,11) if i % 2 == 0]
print(even_num)

squares = [i*i for i in range(1,6)]
print(squares)

num = 7
if num > 1:
    for i in range(2,int(num/2)+1):
        if num % i == 0:
            print("num is not a prime number")
        else:
            print("num is prime number")
            break


#inheritance
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()



