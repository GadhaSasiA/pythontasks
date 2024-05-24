row=5
for i in range(0,row+1):
  for j in range(0,i+1):
   print("*",end='')
  print("")
row=5
for i in range(row,0,-1):
  for j in range(row,i-1):
    print("*",end='') 
  print("")  


class person:
  def __init__(self,name,phone):
    self.name=name
    self.phone=phone

  def address(self):
    print("hai",self.name,self.phone)

a=person("aju",9876543210)
a.address()



class car:
  def __init__(self,name,price,color):
    self.name=name
    self.price=price
    self.color=color

  def start(self):
    print(self.name,"is started")

car1=car("swift",100000,"black")
car2=car("benz",150000,"blue")
car1.start()
print(car1.name,car1.price,car1.color)



class person:
  def __init__(self,name,contact):
    self.name=name
    self.contact=contact

  def address(self):
    print(self.name,self.contact)

class doctor(person):
  pass
class patient(person):
  pass

doc1=doctor("aju",9876543)
pat1=patient("sanu",9876543)
doc1.address()
pat1.address()

    
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")
# Create an instance of Dog
my_dog = Dog('Buddy', 3)

# Access attributes
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Call methods
my_dog.sit()
my_dog.roll_over()

# Create another instance of Dog
your_dog = Dog('Lucy', 5)

# Access attributes
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")

# Call methods
your_dog.sit()
your_dog.roll_over()
